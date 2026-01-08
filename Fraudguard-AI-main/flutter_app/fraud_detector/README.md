# Fraud Detector - Flutter App

Flutter application for fraud detection using ML-powered backend API.

## Setup

1. Install Flutter dependencies:
```bash
flutter pub get
```

2. Configure API URL:
   - Open `lib/services/api_service.dart`
   - Update `baseUrl` based on your setup:
     - Android Emulator: `http://10.0.2.2:8000`
     - iOS Simulator: `http://localhost:8000`
     - Physical Device: `http://YOUR_COMPUTER_IP:8000`

3. Run the app:
```bash
flutter run
```

## Features

- Material 3 UI design
- Form-based input for all 6 transaction features
- Real-time fraud prediction
- Visual feedback (Green for Legit, Red for Fraud)
- Risk score percentage display
- Error handling and loading states


