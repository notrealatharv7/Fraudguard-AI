/// Model representing transaction input data
/// Matches the API request format exactly
class TransactionInput {
  final double transactionAmount;
  final double transactionAmountDeviation;
  final double timeAnomaly;
  final double locationDistance;
  final double merchantNovelty;
  final double transactionFrequency;

  TransactionInput({
    required this.transactionAmount,
    required this.transactionAmountDeviation,
    required this.timeAnomaly,
    required this.locationDistance,
    required this.merchantNovelty,
    required this.transactionFrequency,
  });

  /// Convert to JSON for API request
  Map<String, dynamic> toJson() {
    return {
      'transactionAmount': transactionAmount,
      'transactionAmountDeviation': transactionAmountDeviation,
      'timeAnomaly': timeAnomaly,
      'locationDistance': locationDistance,
      'merchantNovelty': merchantNovelty,
      'transactionFrequency': transactionFrequency,
    };
  }
}


