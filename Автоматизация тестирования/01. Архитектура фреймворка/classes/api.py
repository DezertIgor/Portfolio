import requests
from classes.data import Data

dat = Data().val


class Api:

    def __init__(self, token: dict = dat("token")) -> None:
        self.token = token

    def add_board(self) -> None:
        return requests.post(dat("board_url"),
                             json=dat("board"),
                             cookies=self.token)

    def all_boards(self) -> int:
        return len(requests.get(dat("boards"),
                                cookies=self.token).json()["boards"])

    def last_board(self) -> str:
        return requests.get(dat("boards"),
                            cookies=self.token).json()["boards"][-1]

    def add_card(self) -> dict:
        last = self.last_board()["id"]
        list = requests.post(dat("list_url"),
                             cookies=self.token,
                             json={"idBoard": last,
                                   "name": dat("list_name")}).json()["id"]
        return requests.post(dat("card_url"),
                             cookies=self.token,
                             json={"idList": list,
                                   "name": dat("card")["name"],
                                   "closed": dat("card")["closed"],
                                   "isTemplate": dat("card")["isTemplate"],
                                   "cardRole": dat("card")["cardRole"]}).json()

    def delete_board(self) -> str:
        last = self.last_board()["id"]
        return requests.delete(dat("board_url")+last,
                               cookies=self.token).json()["_value"]

    def last_list(self) -> dict:
        board = self.last_board()["shortLink"]
        return requests.get(dat("board_url")+board+'?fields=id&cards=visible&card_fields=id%2Caddress%2Cbadges%2CcardRole%2Cclosed%2Ccoordinates%2Ccover%2CcreationMethodError%2CdateLastActivity%2Cdesc%2CdescData%2Cdue%2CdueComplete%2CdueReminder%2CidAttachmentCover%2CidBoard%2CidLabels%2CidList%2CidMembers%2CidShort%2CisTemplate%2Clabels%2Climits%2ClocationName%2CmirrorSourceId%2Cname%2Cpinned%2Cpos%2CshortLink%2CshortUrl%2Cstart%2Csubscribed%2Curl&card_attachments=true&card_attachment_fields=id%2Cbytes%2Cdate%2CedgeColor%2CfileName%2CidMember%2CisUpload%2CmimeType%2Cname%2Cpos%2Curl&card_checklists=all&card_checklist_fields=id%2CidBoard%2CidCard%2Cname%2Cpos&card_checklist_checkItems=none&card_customFieldItems=true&card_pluginData=true&card_stickers=true&lists=open&list_fields=id%2Cclosed%2Ccolor%2CcreationMethod%2Cdatasource%2CidBoard%2Climits%2Cname%2Cpos%2CsoftLimit%2Csubscribed%2Ctype',
                            cookies=self.token).json()["lists"][0]

    def last_card(self) -> dict:
        board = self.last_board()["shortLink"]
        return requests.get(dat("board_url")+board+'?fields=id&cards=visible&card_fields=id%2Caddress%2Cbadges%2CcardRole%2Cclosed%2Ccoordinates%2Ccover%2CcreationMethodError%2CdateLastActivity%2Cdesc%2CdescData%2Cdue%2CdueComplete%2CdueReminder%2CidAttachmentCover%2CidBoard%2CidLabels%2CidList%2CidMembers%2CidShort%2CisTemplate%2Clabels%2Climits%2ClocationName%2CmirrorSourceId%2Cname%2Cpinned%2Cpos%2CshortLink%2CshortUrl%2Cstart%2Csubscribed%2Curl&card_attachments=true&card_attachment_fields=id%2Cbytes%2Cdate%2CedgeColor%2CfileName%2CidMember%2CisUpload%2CmimeType%2Cname%2Cpos%2Curl&card_checklists=all&card_checklist_fields=id%2CidBoard%2CidCard%2Cname%2Cpos&card_checklist_checkItems=none&card_customFieldItems=true&card_pluginData=true&card_stickers=true&lists=open&list_fields=id%2Cclosed%2Ccolor%2CcreationMethod%2Cdatasource%2CidBoard%2Climits%2Cname%2Cpos%2CsoftLimit%2Csubscribed%2Ctype',
                            cookies=self.token).json()["cards"][-1]

    def change_card(self) -> dict:
        last = self.last_card()["id"]
        return requests.put(dat("card_url")+last,
                            cookies=self.token,
                            json=dat("change_card")).json()

    def drag_card(self) -> dict:
        card = self.last_card()["id"]
        board = self.last_board()["id"]
        list = requests.post(dat("list_url"),
                             cookies=self.token,
                             json={"idBoard": board,
                                   "name": dat("next_list_name")}).json()["id"]
        return requests.put(dat("card_url")+card,
                            cookies=self.token,
                            json={"idList": list,
                                  "idBoard": board,
                                  "closed": dat("drag_card")["closed"]}).json()

    def delete_card(self) -> None:
        card = self.last_card()["id"]
        return requests.delete(dat("card_url")+card,
                               cookies=self.token)
