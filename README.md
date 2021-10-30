# TextToSymbolConverter
A program that looks through entered text and replaces certain commands with mathematical symbols

Example:   

![image](https://user-images.githubusercontent.com/59739923/139527068-657b7f46-3760-40c1-b9a1-cd2b6dc1ef72.png)

Syntax:
Enter text in the 'INPUT' line. Then the program goes through the text and can make the following changes:
  1) If '^'  is entered, the next character is super-scripted
  2) If '^^' is entered, the next character is sub-scripted
  3) If a command in following way <command> is entered, it's is replaced with respective symbol

Commands:
  1) <0.5> -> ½
  2) <mu> -> μ
  3) <int> -> ∫
  4) <inf> -> ∞
  5) <x> -> ×
  6) </> -> ÷
  7) <Cdel> -> Δ
  8) <sdel> -> δ
