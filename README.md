## 20 Percent : ECC and Transient Errors

|   File   | Purpose  | How to Use  |
| :-------------: |:-------------| :-----|
| **ErrorSim2.0.py** | Creates random binary files, creates errors in them and attempts to correct the errors by comparing multiple versions of the same file | Ensure your computer is equipt to run Python, download a text editor such as Atom to view program |
| ~~ErrorCorrectionSimulation.py~~  |  First iteration of code  |**Dont use**|
|ToDo.txt | For user to input desired percent chance of flip and number of copies, as well as designate how many runs. (ErrorSim2.0 can also randomly generate ToDo.txt should user choose)|  Save .txt file in same folder as program, use format: RunNumber)ChanceErrorAsWholeNum,NumberOfCopies* |
|ForExport.csv | File created to write data into for easy export to Excel or Google Docs| Have a copy or Microsoft Excel available for use or have a Google account. If using Docs: File > Import > Upload > *Do select convert* |

### Corrections and Possible Extensions: 
+ Fix "maximum recursive depth reached" error (is this inherent with recursion and large data sets or flaw of program?) 
+ Add method to calculate actual probability of bit flip based on altitude, hardware type, etc. (See [here](http://lambda-diode.com/opinion/ecc-memory))
+ Add more means of error correction (ex: parity bits)

