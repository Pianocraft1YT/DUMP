#Requires AutoHotkey v2.0

; Paste from clipboard by simulating keystrokes
; Press Ctrl+Alt+Shift+V

^!+v::SendText(A_Clipboard)
