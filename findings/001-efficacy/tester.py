#!/usr/bin/env python3
import sys

def findRepeatedLines(filePath, linesInARow, targetString=None):
  with open(filePath, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f]
  
  for i in range(len(lines) - (linesInARow - 1)):
    if targetString:
      if all(lines[i + j] == targetString for j in range(linesInARow)):
        print(f"First occurrence of '{targetString}' repeated {linesInARow} times starts at line {i + 1}")
        return
    else:
      if all(lines[i] == lines[i + j] for j in range(linesInARow)):
        print(f"First occurrence starts at line {i + 1}: {lines[i]}")
        return
  
  print("No matching repeated lines found.")

def main():
  if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: python script.py <filePath> <linesInARow> [targetString]")
    sys.exit(1)
  
  filePath = sys.argv[1]
  linesInARow = int(sys.argv[2])
  targetString = sys.argv[3] if len(sys.argv) == 4 else None
  
  findRepeatedLines(filePath, linesInARow, targetString)

if __name__ == "__main__":
  main()