Unicode true
!include "MUI2.nsh"
!include "LogicLib.nsh"
!ifndef PROJECT_ROOT
  !error "Pass /DPROJECT_ROOT=<project directory>"
!endif
Name "April, again"
OutFile "${PROJECT_ROOT}\Builds\AprilAgain-Setup.exe"
InstallDir "$LOCALAPPDATA\Programs\AprilAgain"
InstallDirRegKey HKCU "Software\Medissl\AprilAgain" "InstallDir"
RequestExecutionLevel user
SetCompressor zlib
BrandingText "April, again · Medissl"
VIProductVersion "1.0.0.0"
VIAddVersionKey "ProductName" "April, again"
VIAddVersionKey "FileDescription" "April, again Windows installer"
VIAddVersionKey "CompanyName" "Medissl"
VIAddVersionKey "FileVersion" "1.0.0"
VIAddVersionKey "LegalCopyright" "Medissl"
!define MUI_ICON "${PROJECT_ROOT}\Assets\AprilAgain\Art\Title\app_icon_final.ico"
!define MUI_UNICON "${PROJECT_ROOT}\Assets\AprilAgain\Art\Title\app_icon_final.ico"
!define MUI_ABORTWARNING
!define MUI_FINISHPAGE_RUN "$INSTDIR\AprilAgain.exe"
!define MUI_FINISHPAGE_RUN_NOTCHECKED
!define MUI_WELCOMEPAGE_TEXT "Five classmates. One spring. A new beginning.$\r$\n$\r$\nThis installs April, again for your Windows account. Saved stories are kept separately and preserved when the game is removed."
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Section "April, again"
  SetOutPath "$INSTDIR"
  File /r "${PROJECT_ROOT}\Builds\Windows\*.*"
  WriteUninstaller "$INSTDIR\Uninstall.exe"
  FileOpen $0 "$INSTDIR\.april-again-install" w
  FileWrite $0 "AprilAgain/1.0.0"
  FileClose $0
  CreateDirectory "$SMPROGRAMS\April, again"
  CreateShortcut "$SMPROGRAMS\April, again\April, again.lnk" "$INSTDIR\AprilAgain.exe"
  CreateShortcut "$SMPROGRAMS\April, again\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
  WriteRegStr HKCU "Software\Medissl\AprilAgain" "InstallDir" "$INSTDIR"
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain" "DisplayName" "April, again"
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain" "DisplayVersion" "1.0.0"
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain" "Publisher" "Medissl"
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain" "DisplayIcon" "$INSTDIR\AprilAgain.exe"
  WriteRegStr HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain" "UninstallString" '"$INSTDIR\Uninstall.exe"'
  WriteRegDWORD HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain" "NoModify" 1
  WriteRegDWORD HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain" "NoRepair" 1
SectionEnd

Section "Uninstall"
  IfFileExists "$INSTDIR\.april-again-install" 0 done
  Delete "$INSTDIR\AprilAgain.exe"
  Delete "$INSTDIR\UnityPlayer.dll"
  Delete "$INSTDIR\UnityCrashHandler64.exe"
  Delete "$INSTDIR\CREDITS.txt"
  Delete "$INSTDIR\README.txt"
  RMDir /r "$INSTDIR\AprilAgain_Data"
  RMDir /r "$INSTDIR\MonoBleedingEdge"
  RMDir /r "$INSTDIR\D3D12"
  RMDir /r "$INSTDIR\Legal"
  Delete "$INSTDIR\.april-again-install"
  Delete "$INSTDIR\Uninstall.exe"
  RMDir "$INSTDIR"
  Delete "$SMPROGRAMS\April, again\April, again.lnk"
  Delete "$SMPROGRAMS\April, again\Uninstall.lnk"
  RMDir "$SMPROGRAMS\April, again"
  DeleteRegKey HKCU "Software\Medissl\AprilAgain"
  DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\AprilAgain"
  done:
SectionEnd
