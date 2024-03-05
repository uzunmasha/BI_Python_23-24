# Anesthesia for pain.py
This readme describes how to launch the **pain.py** script properly.

System: Windows 11 with WSL2, Ubuntu 22.04.1 LTS
1. On your terminal clone this repo using SSH or HTTPS:
```bash
git clone git@github.com:Python-BI-2023/hw7-environments-uzunmasha.git
``` 
**or**
```bash
git clone https://github.com/Python-BI-2023/hw7-environments-uzunmasha.git
``` 
2. Navigate to the cloned directoryby entering the following command:
```bash
cd hw7-environments-uzunmasha/
```
3. Create a new Conda virtual environment by running:
```bash
conda env create -f uzun_hw7.yml
```
4. Activate the newly created environment with:
```bash
conda activate hw7
```
5. While inside the **hw7** environment, install the required packages. Copy and paste the following commands one by one, or all at once: 
```bash
pip install google
pip install --upgrade google-api-python-client
pip install biopython==1.77
pip install pandas
pip install opencv-python
conda install -c conda-forge pyarrow
```
Launching pyarrow, if you are asked 'Proceed ([y]/n)?', type `y` and press `Enter`.

6. In your terminal, execute the script by typing:
```bash
python pain.py
```
You will encounter an error.

7. In the error message, locate the line that says **raise ValueError("index cannot be a set")**. Above this line, find the line that starts with **File "/**. Copy the full path to the **frame.py** file without quotes. For example:
**/home/uzunm/miniconda3/envs/hw7/lib/python3.12/site-packages/pandas/core/frame.py**

8. Open the **frame.py** file by typing the following command, replacing **/full/path/to/frame.py/** with your copied path:
```bash
nano /full/path/to/frame.py/
```

9. After that, you will see the code in file **frame.py**. In the opened file type simultaneously `Ctrl` , `Shift` and ` - ` on your keyboard.

10. Navigate to line 699 by typing `699` and pressing `Enter`.

11. Comment out the problematic code by adding `#` at the beginning of the line that starts with if and the next line that starts with raise. It should look like
```python
#  if isinstance(index, set):
#     raise ValueError("index cannot be a set")
```
12. Save and exit the frame.py file by pressing `Ctrl` + `O`, followed by `Enter`, and then `Ctrl` + `X`.

13. In the terminal, re-run the script with the following command:
```bash
python pain.py
```
14. If everything is working correctly, you should see the message:
```
Всё работает, ты больш(ой/ая) молодец!!!
```
This means you are amazing, and can now go to the rest!
I, for example, took a bath and slept for 10 hours yesterday. It was amazing! I strongly recommend!
