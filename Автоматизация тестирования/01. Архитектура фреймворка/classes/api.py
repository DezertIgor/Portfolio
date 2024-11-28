import requests
from classes.data import Data
import allure

dat = Data().val


class Api:

    def __init__(self, token: dict = dat("token")) -> None:
        self.token = token

    @allure.step("Создание доски")
    def add_board(self) -> None:
        """
        Создаёт новую доску
        """
        return requests.post(dat("board_url"),
                             json=dat("board"),
                             cookies=self.token)

    @allure.step("Выявление количества досок")
    def all_boards(self) -> int:
        """
        Возвращает количество всех активных досок пользователя
        """
        return len(requests.get(dat("boards"),
                                cookies=self.token).json()["boards"])

    @allure.step("Получение информации о последней из созданных досок")
    def last_board(self) -> str:
        """
        Возвращает последнюю активную из созданных досок
        """
        return requests.get(dat("boards"),
                            cookies=self.token).json()["boards"][-1]

    @allure.step("Добавление карточки")
    def add_card(self) -> dict:
        """
        Создаёт новый список и в него добавляет новую карточку
        """
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

    @allure.step("Удаление доски")
    def delete_board(self) -> str:
        """
        Удаляет последнюю активную созданную доску
        """
        last = self.last_board()["id"]
        return requests.delete(dat("board_url")+last,
                               cookies=self.token).json()["_value"]

    @allure.step("Получение информации о последнем списке")
    def last_list(self) -> dict:
        """
        Возвращает последний созданный список (активный)
        """
        board = self.last_board()["shortLink"]
        return requests.get(dat("board_url")+board+'?fields=id&cards=visible&card_fields=id%2Caddress%2Cbadges%2CcardRole%2Cclosed%2Ccoordinates%2Ccover%2CcreationMethodError%2CdateLastActivity%2Cdesc%2CdescData%2Cdue%2CdueComplete%2CdueReminder%2CidAttachmentCover%2CidBoard%2CidLabels%2CidList%2CidMembers%2CidShort%2CisTemplate%2Clabels%2Climits%2ClocationName%2CmirrorSourceId%2Cname%2Cpinned%2Cpos%2CshortLink%2CshortUrl%2Cstart%2Csubscribed%2Curl&card_attachments=true&card_attachment_fields=id%2Cbytes%2Cdate%2CedgeColor%2CfileName%2CidMember%2CisUpload%2CmimeType%2Cname%2Cpos%2Curl&card_checklists=all&card_checklist_fields=id%2CidBoard%2CidCard%2Cname%2Cpos&card_checklist_checkItems=none&card_customFieldItems=true&card_pluginData=true&card_stickers=true&lists=open&list_fields=id%2Cclosed%2Ccolor%2CcreationMethod%2Cdatasource%2CidBoard%2Climits%2Cname%2Cpos%2CsoftLimit%2Csubscribed%2Ctype',
                            cookies=self.token).json()["lists"][0]

    @allure.step("Получение информации о последней созданной карточке")
    def last_card(self) -> dict:
        """
        Возвращает последнюю созданную карточку
        """
        board = self.last_board()["shortLink"]
        return requests.get(dat("board_url")+board+'?fields=id&cards=visible&card_fields=id%2Caddress%2Cbadges%2CcardRole%2Cclosed%2Ccoordinates%2Ccover%2CcreationMethodError%2CdateLastActivity%2Cdesc%2CdescData%2Cdue%2CdueComplete%2CdueReminder%2CidAttachmentCover%2CidBoard%2CidLabels%2CidList%2CidMembers%2CidShort%2CisTemplate%2Clabels%2Climits%2ClocationName%2CmirrorSourceId%2Cname%2Cpinned%2Cpos%2CshortLink%2CshortUrl%2Cstart%2Csubscribed%2Curl&card_attachments=true&card_attachment_fields=id%2Cbytes%2Cdate%2CedgeColor%2CfileName%2CidMember%2CisUpload%2CmimeType%2Cname%2Cpos%2Curl&card_checklists=all&card_checklist_fields=id%2CidBoard%2CidCard%2Cname%2Cpos&card_checklist_checkItems=none&card_customFieldItems=true&card_pluginData=true&card_stickers=true&lists=open&list_fields=id%2Cclosed%2Ccolor%2CcreationMethod%2Cdatasource%2CidBoard%2Climits%2Cname%2Cpos%2CsoftLimit%2Csubscribed%2Ctype',
                            cookies=self.token).json()["cards"][-1]

    @allure.step("Изменение фона карточки")
    def change_card(self) -> dict:
        """
        Изняет цвет заднего фона карточки
        """
        last = self.last_card()["id"]
        return requests.put(dat("card_url")+last,
                            cookies=self.token,
                            json=dat("change_card")).json()

    @allure.step("Перемещение карточки в другой список")
    def drag_card(self) -> dict:
        """
        Перемещает последнюю созданную карточку в другой список (последний из
        созданных и активный) и возвращает информацию этой карточки
        """
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

    @allure.step("Удаление карточки")
    def delete_card(self) -> None:
        """
        Удаляет последнюю из созданных карточек
        """
        card = self.last_card()["id"]
        return requests.delete(dat("card_url")+card,
                               cookies=self.token)
