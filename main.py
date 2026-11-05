from datetime import datetime
from random import randint
from fastapi import FastAPI, HTTPException, Request, Response
from typing import Any


app = FastAPI(root_path="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

data : any = [
    {
        "campaign_id": 1,
        "name": "Summer Launch",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    },
    {
        "campaign_id": 2,
        "name": "Black Fridays",
        "due_date": datetime.now(),
        "created_at": datetime.now()
    }
]

# Campaigns
# - campaign_id
# - name
# - due_date
# - created_at

@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns": data}

# get single campaign
@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("compaign_id") == id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404)

# Creating Campaign
@app.post("/campaigns", status_code=201)
async def create_campaigns(body: dict[str, Any]):
    # body = await request.json()
    new: Any = {
        "compaign_id": randint(100,1000),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at": datetime.now()
    }

    data.append(new)
    return {"campaign": new}

# Update a campaign
@app.put("/campaigns/{id}")
async def update_campaign(id: int, body: dict[str, Any]):
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
            updated: Any = {
                "compaign_id": id,
                "name": body.get("name"),
                "due_date": body.get("due_date"),
                "created_at": campaign.get("created_at")
            }
            data[index] = updated
            return {"Campaign": updated}
    raise HTTPException(status_code=404)


# Delete a Campaign
@app.delete("/campaigns/{id}")
async def update_campaign(id: int): 
    for index, campaign in enumerate(data):
        if campaign.get("campaign_id") == id:
           data.pop(index)
           return Response(status_code=204)
    raise HTTPException(status_code=404)