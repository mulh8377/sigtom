import asyncio
import logging
from influxdb_client import InfluxDBClient

class SignalEngine:
    def __init__(self, user: str, passwrd: str, org: str) -> None:
        self.name = "signals"
        self.host = None
        self.port = None
        self.username = user
        self.password = passwrd
        self.org = org
        self.ssl = True
        self.verify_ssl = True
        self.client = None

    def setup(self, _host, _port) -> None:
        self.host = _host
        self.port = _port
        self.client = InfluxDBClient(url="http://172.18.0.4:8086", token="test", org=self.org)
        #self.client.create_database(self.name)
        #self.client.switch_database(self.name)

    def shutdown(self) -> None:
        self.client.close()

    def write(self, field) -> bool:
        # client.write_api
        logging.debug(f"writing to bucket: {self.name} w/ data: {field}")

        writer = self.client.write_api()

        writer.write(bucket=self.name, record=field)

        writer.close()


    async def read(self, bucket_name: str, query):
        # client.query_api
        asyncio.sleep(1)

        search_bucket = f'from(bucket:"{bucket_name}")'

        logging.debug(f"searching: {search_bucket} query:{query}")
    

    async def delete(self, bucket_name: str, predicate, start, end):
        # client.delete_api
        asyncio.sleep(1)

        logging.debug(f"deleting {predicate} in the range {start} - {end} from {bucket_name}")