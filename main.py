import uuid

from fastapi import FastAPI, HTTPException
from typing import List
from models.reservation_model import agentReservation, passenger, recordLocator, hub, airline
from repositories.reservationrepository import get_all_agent_reservations, get_all_airline_details, get_all_hub_info, \
    get_airline_details_by_id, get_all_passenger_details, get_all_record_locators, get_reservation_by_id, \
    get_hub_info_by_id, get_passenger_details_by_id, get_record_locators_by_id, create_agent_reservation, create_airline, \
    create_hub, create_passenger, create_record_locator, update_agent_reservation, update_airline_details, update_hub_details, \
    update_passenger_details, update_recordlocator_details, delete_agent_reservation, delete_airlines, delete_hubs, delete_passengers, \
    delete_record_locators

app = FastAPI()


@app.get("/agentreservation")
def get_all_agent_reservations_api() -> List[agentReservation]:
    return get_all_agent_reservations()

@app.get("/airlinedetails")
def get_all_airline_details_api() -> List[airline]:
    return get_all_airline_details()

@app.get("/hubinfo")
def get_all_hub_info_api() -> List[hub]:
    return get_all_hub_info()

@app.get("/passengerdetails")
def get_all_passenger_details_api() -> List[passenger]:
    return get_all_passenger_details()

@app.get("/recordlocators")
def get_all_record_locators_api() -> List[recordLocator]:
    return get_all_record_locators()

@app.post("/agentreservation")
def create_agent_reservations_api(agentreservation: agentReservation) -> agentReservation:
    return create_agent_reservation(agentreservation)

@app.post("/airlinedetails")
def create_airline_details_api(airlines: airline) -> airline:
    return create_airline(airlines)

@app.post("/hubinfo")
def create_hub_details_api(hubs: hub) -> hub:
    return create_hub(hubs)

@app.post("/passengerdetails")
def create_passenger_details_api(passengers: passenger) -> passenger:
    return create_passenger(passengers)

@app.post("/recordlocators")
def create_record_locators_api(recordlocators: recordLocator) -> recordLocator:
    return create_record_locator(recordlocators)

@app.get("/agentreservation/{reservation_id}")
def get_agent_reservations_api(reservation_id: str) -> agentReservation:
    uid = uuid.UUID(reservation_id)
    reservationId = get_reservation_by_id(uid)
    return reservationId

@app.get("/airlinedetails/{airline_id}")
def get_airline_details_api(airline_id: str) -> airline:
    uid = uuid.UUID(airline_id)
    airlineId = get_airline_details_by_id(uid)
    return airlineId

@app.get("/hubinfo/{hub_id}")
def get_hub_info_api(hub_id: str) -> hub:
    uid = uuid.UUID(hub_id)
    hubId = get_hub_info_by_id(uid)
    return hubId

@app.get("/passengerdetails/{passenger_id}")
def get_passenger_details_api(passenger_id: str) -> passenger:
    uid = uuid.UUID(passenger_id)
    passengerId = get_passenger_details_by_id(uid)
    return passengerId

@app.get("/recordlocators/{record_locator_id}")
def get_record_locators_api(record_locator_id: str) -> recordLocator:
    uid = uuid.UUID(record_locator_id)
    recordlocatorId = get_record_locators_by_id(uid)
    return recordlocatorId

@app.put("/agentreservation/{reservation_id}")
def update_agent_reservations_api(reservation_id: str, agentreservation: agentReservation) -> agentReservation:
    if reservation_id != agentreservation.reservation_id:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_agent_reservation(agentreservation)

@app.put("/airlinedetails/{airline_id}")
def update_airline_details_api(airline_id: str, airlines: airline) -> airline:
    if airline_id != airline.airline_id:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_airline_details(airlines)

@app.put("hubinfo/{hub_id}")
def update_hub_info_api(hub_id: str, hubs: hub) -> hub:
    if hub_id != hub.hub_id:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_hub_details(hubs)

@app.put("passengerdetails/{passenger_id}")
def update_passenger_details_api(passenger_id: str, passengers: passenger) -> passenger:
    if passenger_id != passenger.passenger_id:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_passenger_details(passengers)

@app.put("/recordlocators/{record_locator_id}")
def update_record_locators_api(record_locator_id: str, recordlocators: recordLocator) -> recordLocator:
    if record_locator_id != recordLocator.record_locator_id:
        raise HTTPException(status_code=400, detail="path id and object id must match")
    return update_recordlocator_details(recordlocators)

@app.delete("/agentreservation/{reservation_id}")
def delete_agent_reservation_api(reservation_id: str):
    uid = uuid.UUID(reservation_id)
    delete_agent_reservation(uuid)

@app.delete("/airlinedetails/{airline_id}")
def delete_airline_details_api(airline_id: str):
    uid = uuid.UUID(airline_id)
    delete_airlines(uid)

@app.delete("/hubinfo/{hub_id}")
def delete_hub_info_api(hub_id: str):
    uid = uuid.UUID(hub_id)
    delete_hubs(uid)

@app.delete("/passengerdetails/{passenger_id}")
def delete_passenger_details_api(passenger_id: str):
    uid = uuid.UUID(passenger_id)
    delete_passengers(uid)

@app.delete("/recordlocators/{record_locator_id}")
def delete_record_locators_api(record_locator_id: str):
    uid = uuid.UUID(record_locator_id)
    delete_record_locators(uid)

