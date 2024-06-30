from typing import Dict, Tuple, List
from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_link(self, link_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"],
            )
        )
        self.__conn.commit()

    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE trip_id = ?''', (trip_id,)
        )
        links = cursor.fetchall()
        return links
