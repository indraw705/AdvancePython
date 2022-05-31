import json
import requests

auth = "Bearer eyJhbGciOiJSUzUxMiJ9.eyJpYXQiOjE2NTM5NzMzNzQsImV4cCI6MTY1Mzk4Nzc3NCwiaXNzIjoiaW9jX2ludGVybmFsX3NlcnZpY2UiLCJhdWQiOiJpb2Mtd2ViLXNlcnZpY2UifQ.dlEbDmDXJmRL2hn7tjkkLgmhI3RGhU1pq2g4MKNEhdC7uAIE3M6fHc9bV-0nQHF-MX8FaHQruZiSYthEWw0_TG4wlxDOXKZHoZh3YuT9O3xG9ukrBIuvuRVfHrKSESdooEzBM_ZFQwV_yNm37s7aVBy6972mkrYU33MliIV0QICAJ6c-1qrsNujDzc_QCK8Ro1zWp7FAlKwUaep-PhPpMPzMVRITg7Hd-emVV0G-ipoxBdqVInnO-D2k7uvV_GGfRalFcTCFq9Iyabz5nv5bbVEwAmnLVUvhTcfnTnHAt3Rc39t9kQ-VG5N1FFqAaN5bh-e5sl7n7bVHhCnNgwgkpg"


def write_to_file(date, group_by, resp):
    resp = str(resp).replace(",", ",\n")
    with open("QoQ.json", "a") as file_object:
        file_object.write(date + " >> " + group_by + "\n\n")
        file_object.write(str(resp))
        file_object.write("\n\n")


def get_agent_wise_count(resp, uuid):
    count = resp.get(uuid)
    if count:
        return count
    else:
        return 0


def getQoQStats_EventsCount_by_type(date, group_by):
    url = "https://kubelb.p13.eng.sjc01.qualys.com/ioc-ws/events/count?filter=(dateTime%3A%5B%22" + date + "T00%3A00%3A00.000Z%22..%22" + date + "T11%3A59%3A59.999Z%22%5D)&groupBy=" + group_by + "&state=false"
    headers = {"customerId": "2dd48beb-d268-5821-83bf-8cfa50611ea1",
               "S2S-Authorization": auth}
    response = requests.get(url, headers=headers, verify=False)
    resp = json.loads(response.text)
    write_to_file(date, group_by, resp)


def getQoQStats_EventsCount_by_agent(date, group_by):
    url = "https://kubelb.p13.eng.sjc01.qualys.com/ioc-ws/events/count?filter=(dateTime%3A%5B%22" + date + "T00%3A00%3A00.000Z%22..%22" + date + "T11%3A59%3A59.999Z%22%5D)&groupBy=" + group_by + "&state=false"
    headers = {"customerId": "2dd48beb-d268-5821-83bf-8cfa50611ea1",
               "S2S-Authorization": auth}
    response = requests.get(url, headers=headers, verify=False)
    resp = json.loads(response.text)
    print(resp)
    count1 = get_agent_wise_count(resp, "00fecc00-41a0-446e-9656-c858ff33d1d9")
    count2 = get_agent_wise_count(resp, "320a6b00-5961-4f2e-a4c1-6f4f8e61b8b4")
    count3 = get_agent_wise_count(resp, "75d72401-32ec-41ee-9488-cef0767e588c")
    count4 = get_agent_wise_count(resp, "3c2e9c9a-3859-4aac-b28c-725de497c2b2")
    count5 = get_agent_wise_count(resp, "e3e8cf0d-9b08-4e40-9fa6-a84854276707")
    count6 = get_agent_wise_count(resp, "83f2560e-2d80-4aa0-899f-eeeebe291282")
    count7 = get_agent_wise_count(resp, "16625b0b-768d-49f8-9782-c1d1bfeda43f")
    count8 = get_agent_wise_count(resp, "0dc0b321-e8ec-4cb7-ba3a-dfc7b44b348d")

    with open("QoQ.json", "a") as file_object:
        file_object.write(date + " >> " + group_by + "\n\n")
        file_object.write((str(count1)) + ":\n")
        file_object.write((str(count2)) + ":\n")
        file_object.write((str(count3)) + ":\n")
        file_object.write((str(count4)) + ":\n")
        file_object.write((str(count5)) + ":\n")
        file_object.write((str(count6)) + ":\n")
        file_object.write((str(count7)) + ":\n")
        file_object.write((str(count8)) + ":\n")


if __name__ == '__main__':
    for i in range(30, 31):
        getQoQStats_EventsCount_by_type("2022-05-" + str(i), "process.name")
        getQoQStats_EventsCount_by_type("2022-05-" + str(i), "file.name")
        getQoQStats_EventsCount_by_type("2022-05-" + str(i), "network.process.name")
        getQoQStats_EventsCount_by_agent("2022-05-" + str(i), "asset.agentid")
