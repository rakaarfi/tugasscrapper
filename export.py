import pandas as pd

def exportPandas(datas, filename):
  df = pd.DataFrame(datas)
  print(f"Exporting to DataFrame for {filename}")
  
  df.to_excel(f'{filename}.xlsx', index=False)

  print(f"Extract to {filename}.xlsx finished.")
  return df