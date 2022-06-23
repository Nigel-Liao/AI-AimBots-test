
; Configuration
#SingleInstance force ;It allows to run only one at the same time.
SetTitleMatchMode, 2 ;Matching for window title.
#ifwinactive, Apex Legends ;Active only when in PUBG.
  #NoEnv
  #KeyHistory, 0
  #SingleInstance force
  #MaxThreadsBuffer on
  #Persistent
  ;#NoTrayIcon 
  SetBatchLines -1 
  ListLines Off
  SetWorkingDir %A_ScriptDir%
  ;SetKeyDelay, -1, -1
  ;SetMouseDelay, -1
  ;SetDefaultMouseSpeed, 0
  ;SetWinDelay, -1

  Gui, Font, cAqua
  Gui, Font, s15
  Gui, Add, Text, x50 y60, Script running

  Gui, -AlwaysOnTop
  Gui, Color, Black
  Gui, Show, w200 h150, No Recoil Script

  ; Variables
  isMouseShown() ;To suspend script when mouse is visible.
  ;Compensation = 1 ;Var for compensation when autofiring.
  ;compVal = 1 ;Compensation value.

  ; Suspends if mouse is visible
  isMouseShown() ;It suspends the script when mouse is visible (inventory, menu).
  {
    StructSize := A_PtrSize + 16
    VarSetCapacity(InfoStruct, StructSize)
    NumPut(StructSize, InfoStruct)
    DllCall("GetCursorInfo", UInt, &InfoStruct)
    Result := NumGet(InfoStruct, 8)

    if Result > 1
      Return 1
    else
      Return 0
  }
  Loop
  {
    if isMouseShown() == 1
      Suspend On
    else
      Suspend Off
    Sleep 1
  }

  ; AutoFire
  ~$*LButton:: ;AutoFire
    Loop
    {
      GetKeyState, LButton, LButton, P
      if LButton = U
        Break
      MouseClick, Left,,, 1
      Gosub, RandomSleep ;Call to RandomSleep.
      mouseXY(0, 1) ;If active, call to Compensation.
    }
  Return
  RandomSleep: ;Random timing between clicks, just in case.
    Random, random, 14, 25
    Sleep %random%-5
  Return

  ; Compensation
  mouseXY(x,y) ;Moves the mouse down to compensate recoil (value in compVal var).
  {
    DllCall("mouse_event",uint,1,int,x,int,y,uint,0,int,0)
  }

  ; Tooltips
  ToolTip(label) ;Function to show a tooltip when activating, deactivating or changing values.
  {
    ToolTip, %label%, 930, 650 ;Tooltips are shown under crosshair for FullHD monitors.
    SetTimer, RemoveToolTip, 1300 ;Removes tooltip after 1.3 seconds.
  return
  RemoveToolTip:
    SetTimer, RemoveToolTip, Off
    ToolTip
  Return
}

