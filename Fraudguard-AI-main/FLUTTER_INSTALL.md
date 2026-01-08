# Flutter Installation Guide for Windows

## Quick Installation Steps

### Option 1: Using Git (Recommended)

1. **Install Git** (if not already installed):
   - Download: https://git-scm.com/download/win
   - Install with default settings

2. **Clone Flutter SDK:**
   ```powershell
   cd C:\
   git clone https://github.com/flutter/flutter.git -b stable
   ```

3. **Add Flutter to PATH:**
   - Press `Win + X` and select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "User variables", find "Path" and click "Edit"
   - Click "New" and add: `C:\flutter\bin`
   - Click "OK" on all dialogs

4. **Restart PowerShell/Terminal**

5. **Verify Installation:**
   ```powershell
   flutter --version
   flutter doctor
   ```

### Option 2: Direct Download

1. **Download Flutter SDK:**
   - Go to: https://flutter.dev/docs/get-started/install/windows
   - Download the latest stable release ZIP file

2. **Extract:**
   - Extract to `C:\flutter` (or your preferred location)

3. **Add to PATH** (same as Option 1, step 3)

4. **Restart PowerShell/Terminal**

5. **Verify:**
   ```powershell
   flutter --version
   flutter doctor
   ```

## Additional Requirements

### Android Development (for Android apps)

1. **Install Android Studio:**
   - Download: https://developer.android.com/studio
   - Install with default settings

2. **Install Android SDK:**
   - Open Android Studio
   - Go to: Tools → SDK Manager
   - Install Android SDK Platform-Tools

3. **Accept Android Licenses:**
   ```powershell
   flutter doctor --android-licenses
   ```

### VS Code (Optional but Recommended)

1. **Install VS Code:**
   - Download: https://code.visualstudio.com/

2. **Install Flutter Extension:**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Flutter" and install

## Verify Everything Works

```powershell
flutter doctor
```

This will show what's installed and what needs to be configured.

## After Installation

Once Flutter is installed, you can run the app:

```powershell
cd flutter_app\fraud_detector
flutter pub get
flutter run
```

## Troubleshooting

**"flutter: command not found"**
- Make sure Flutter is added to PATH
- Restart your terminal/PowerShell
- Try: `C:\flutter\bin\flutter --version` (if installed to C:\flutter)

**"Android licenses not accepted"**
```powershell
flutter doctor --android-licenses
# Press 'y' to accept all licenses
```

**Need help?**
- Flutter Docs: https://flutter.dev/docs
- Flutter Community: https://flutter.dev/community

