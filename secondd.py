#%%
import win32com.client
fso = win32com.client.Dispatch("Scripting.FileSystemObject")
#%%
fldr = fso.GetFolder("c:\\windows\\system32")
print(fldr.Name)
                     
#%%
[12,34]

#%%
'qwerty-qwerty'