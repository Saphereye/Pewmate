# PEWMATE
Program that looks through Entered text and replaces certain commands With MAthEmatical symbols

Example:   

![image](https://user-images.githubusercontent.com/59739923/139571439-4a4d92f8-334e-48bf-b355-8ca12e57cce6.png)

Syntax:
Enter text in the 'INPUT' line. Then the program goes through the text and can make the following changes:
  1) If '^'  is entered, the next character is super-scripted
  2) If '^^' is entered, the next character is sub-scripted
  3) If a command in following way <command> is entered, it's is replaced with respective symbol

Commands(can be seen on typing 'help' in INPUT):
  1) <0.5>   -> ½
  2) \<mu>   -> μ
  3) \<int>  -> ∫
  4) \<inf>  -> ∞
  5) \<x>    -> ×
  6) \</>    -> ÷
  7) \<Cdel> -> Δ
  8) \<sdel> -> δ

Errors Identification(Can view all possible erros on typing 'errors')
  1) '^' -> 'Error[1]:Empty argument for superscript'
  2) '^^'-> 'Error[2]:Empty argument for subscript'
