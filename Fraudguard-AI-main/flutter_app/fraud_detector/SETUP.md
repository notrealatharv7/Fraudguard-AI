# Flutter App Setup & Run Guide

## Prerequisites

1. **Install Flutter** (if not already installed):
   - Download from: https://flutter.dev/docs/get-started/install/windows
   - Extract and add Flutter to your PATH
   - Verify installation: `flutter doctor`

2. **Install Android Studio** (for Android emulator) or **Xcode** (for iOS - macOS only)

## Quick Start

### Step 1: Navigate to Flutter App Directory

```powershell
cd flutter_app\fraud_detector
```

### Step 2: Install Dependencies

```powershell
flutter pub get
```

### Step 3: Configure API URL

**IMPORTANT:** Update the API URL in `lib/services/api_service.dart` based on your setup:

**For Android Emulator:**
```dart
static const String baseUrl = 'http://10.0.2.2:8000';
```

**For iOS Simulator:**
```dart
static const String baseUrl = 'http://localhost:8000';
```

**For Physical Device:**
1. Find your computer's IP address:
   ```powershell
   ipconfig
   # Look for IPv4 Address (e.g., 192.168.1.100)
   ```
2. Update the URL:
   ```dart
   static const String baseUrl = 'http://192.168.1.100:8000';  // Replace with your IP
   ```

### Step 4: Start the Backend API

Make sure the backend is running first:

```powershell
# From project root
python start_backend.py
```

### Step 5: Run Flutter App

**Check available devices:**
```powershell
flutter devices
```

**Run on Android Emulator:**
```powershell
flutter run
```

**Run on specific device:**
```powershell
flutter run -d <device-id>
```

**Run in Chrome (for web testing):**
```powershell
flutter run -d chrome
```

## Troubleshooting

### Flutter not found
- Add Flutter to your PATH environment variable
- Restart your terminal/PowerShell

### Backend connection errors
- Ensure backend is running: `http://localhost:8000/health`
- Check API URL in `api_service.dart`
- For physical device: Use your computer's IP, not `localhost`

### Build errors
```powershell
flutter clean
flutter pub get
flutter run
```

## Testing the App

1. Fill in all 6 transaction fields
2. Click "Check for Fraud"
3. See the result:
   - **Green card** = Legitimate transaction
   - **Red card** = Fraud detected
   - Risk score percentage displayed

