+++
title = 'Azure Purview Non Enterprise Account'
date = 2024-11-14T23:32:57+08:00
draft = false
+++

Azure Purview - Would this time works?  

I can't recall how many time I've been trying out of the box Azure offering for Master Data Governance product under Microsoft Azure.  
The first "promising" option was Azure Data Catalog.  
The sales person keep saying that it could auto scan our estate, auto catalog, and magic mushroom high features.  

Well, we tried.  
Yes, it's able to scan our Azure SQL, but Data Lake Gen2?  
How about PowerBI?  
How about Project based Data Governance, not enterprise wide?  
Naah... nope.. stay away demon... 😈
And don't start talking about the license... complicated brother!

Then I was looking Apache Atlas because we are using HDInsight, Hive, Data Lake, HDFS.  😎   
TBH, it looks promising. 🤔  
However! It's IaaS hosted, need VMs, need Public IP, yada yada yada....   
REJECTED! 🙅‍♂️   

*"Ladies and Gentlemen, here comes the new challenger…"*🌠    
**AZURE PURVIEW**   

Underneath the skin, it's actually running on Apache Atlas!!!  
Boy oh boy... It's clean, neat, and attractive!   
It has REST API! It has Python library which could talk to it!  
It has data scanner, collection, proper security model!  
I can't wait to play more with this baby 😎   

I quickly realized that...   
The first Purview account that you deploy in your tenant (read it correctly **TENANT!**)  
YES! It will be enterprise wide deployment ***BOOOO!!!***   

We learned the hard way, we deploy it on dev environment, and....   
What the heck! It kind of scan whole tenant! 🤬   

Then we keep trying and we quickly figured out that the subsequence accounts that we deploy, it then becomes our own project governance.
Why MICROSOFT, WHY!!?!?!?   

Anyway, 'nuf for today.
I shall share my journey in near future!  

#Azure #Purview #Experience #DataGovernance

![Data Catalog](/images/catalog.jpg "Photo by cottonbro studio")