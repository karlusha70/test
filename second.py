#%%
import win32com.client
fso = win32com.client.Dispatch("Scripting.FileSystemObject")
#%%
fldr = fso.GetFolder("c:\\windows\\system32")
print(fldr.Name)
                     
