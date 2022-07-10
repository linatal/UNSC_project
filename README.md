# UNSC_project

Processing skripts for  UN Security Council Meeting Records corpus from Schönfeld et al. 2019: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KGVSYH

### Exclude files with presidential speeches
Input is dir-path to raw files (speaker name must be included in string). Creates two folders with excluded speeches and selected speeches.
```python exclude_presidential_spchs.py --input $DIR_PATH``` 

### Text preprocessing
Skipt to delete string until first column (speaker-name, language) and linebreaks within paragraphs. WPath-input can point to directory or file (each file within folder will be processed). The input-file will be overwritten.  
```python delete_linebreaks.py --input $INPUT_PATH``` 

### Paragraph splitting
Splits paragraphs in string into seperate files. For each paragraph, a new file is created. Path-input can point to directory or file.  
```python split_paragraphs.py --input $INPUT_PATH``` 


### Literature

The UN Security Council Debates.
Schoenfeld, Mirco; Eckhard, Steffen; Patz, Ronny; Meegdenburg, Hilde van; Pires, Antonio, 2019, "The UN Security Council Debates", https://doi.org/10.7910/DVN/KGVSYH, Harvard Dataverse, V5, UNF:6:zwZdSPbcmfAbjIiKdqzgig== [fileUNF] 