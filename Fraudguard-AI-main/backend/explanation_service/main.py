from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="Explanation AI Service",
    description="Generates explanations for fraud predictions.",
    version="1.0.0"
)

# Load the Hugging Face model on startup
# This can take a moment, but it's only done once.
explainer = pipeline("text-generation", model="distilgpt2")

class PredictionDetails(BaseModel):
    transactionAmount: float
    transactionAmountDeviation: float
    timeAnomaly: float
    locationDistance: float
    merchantNovelty: float
    transactionFrequency: float
    isFraud: bool
    riskScore: float

class ExplanationResponse(BaseModel):
    explanation: str

@app.post("/explain", response_model=ExplanationResponse)
async def get_explanation(details: PredictionDetails):
    """Generates a human-readable explanation for a fraud prediction."""
    try:
        # Use the improved prompt function that generates context-aware explanations
        explanation = create_prompt(details)
        return ExplanationResponse(explanation=explanation)
    except Exception as e:
        return ExplanationResponse(explanation=f"Could not generate explanation: {e}")

def create_prompt(details: PredictionDetails) -> str:
    """Creates a structured prompt for generating a context-aware explanation."""
    status = "fraudulent" if details.isFraud else "legitimate"
    
    # Analyze the actual transaction factors
    factors = []
    if details.transactionAmountDeviation > 0.5:
        factors.append(f"high amount deviation ({details.transactionAmountDeviation:.2f})")
    elif details.transactionAmountDeviation < 0.2:
        factors.append(f"normal amount deviation ({details.transactionAmountDeviation:.2f})")
    
    if details.locationDistance > 50:
        factors.append(f"very far location ({details.locationDistance:.1f}km)")
    elif details.locationDistance > 20:
        factors.append(f"distant location ({details.locationDistance:.1f}km)")
    elif details.locationDistance < 5:
        factors.append(f"nearby location ({details.locationDistance:.1f}km)")
    
    if details.merchantNovelty > 0.7:
        factors.append("new/unknown merchant")
    elif details.merchantNovelty < 0.3:
        factors.append("familiar merchant")
    
    if details.timeAnomaly > 0.6:
        factors.append("unusual transaction time")
    elif details.timeAnomaly < 0.3:
        factors.append("normal transaction time")
    
    if details.transactionFrequency < 3:
        factors.append("low transaction frequency")
    elif details.transactionFrequency > 10:
        factors.append("high transaction frequency")
    
    factors_text = ", ".join(factors) if factors else "mixed indicators"
    
    # Generate explanation based on status and factors
    if details.isFraud:
        explanation = f"This transaction is flagged as {status} (risk: {details.riskScore*100:.0f}%) because it shows {factors_text}."
        if details.transactionAmountDeviation > 0.5:
            explanation += " The transaction amount significantly deviates from the user's typical spending patterns."
        if details.locationDistance > 20:
            explanation += " The location is far from where the user typically makes transactions."
        if details.merchantNovelty > 0.7:
            explanation += " The merchant is unfamiliar, which increases fraud risk."
        if details.timeAnomaly > 0.6:
            explanation += " The transaction occurred at an unusual time."
    else:
        explanation = f"This transaction appears {status} (risk: {details.riskScore*100:.0f}%) based on {factors_text}."
        if details.transactionAmountDeviation < 0.3:
            explanation += " The amount is consistent with the user's normal spending behavior."
        if details.locationDistance < 10:
            explanation += " The transaction occurred at a familiar location."
        if details.merchantNovelty < 0.4:
            explanation += " The merchant is known and frequently used by the user."
        if details.timeAnomaly < 0.4:
            explanation += " The transaction timing aligns with typical user patterns."
    
    return explanation

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
