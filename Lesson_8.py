{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "連線成功\n",
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'\n",
    "response = requests.request('GET',url)\n",
    "if response.status_code == 200:\n",
    "    print(\"連線成功\")\n",
    "    all_data = response.json()\n",
    "    print(type(all_data))\n",
    "else:\n",
    "    print(f\"連線失敗:{response.status_code}\")\n",
    "\n",
    "\n",
    "\n",
    "dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])\n",
    "min=int(input(\"請輸入要查詢的可借數量:\"))\n",
    "mask = dataFrame['sbi'] <= min\n",
    "mask_dataFrame = dataFrame[mask]\n",
    "mask_dataFrame.to_csv('可借小於3的站點.csv')\n",
    "filename = f'可借小於{min}的站點.xlsx'\n",
    "mask_dataFrame.to_excel(filename)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
