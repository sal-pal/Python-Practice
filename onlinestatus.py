statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):

    online_count = 0
    statuses = statuses.values() 
    
    for status in statuses:
        if status == "online":
            online_count += 1
            
    return online_count
