import argparse
import asyncio
import logging
import ssl
import sys
from getpass import getpass
from slixmpp import ClientXMPP

class StarfaceBot(ClientXMPP):
    def __init__(self, jid, password, recipient, message_text):
        super().__init__(jid, password)
        self.recipient = recipient
        self.message_text = message_text
        self.add_event_handler("session_start", self.session_start)

    async def session_start(self, event):
        self.send_presence()
        await self.get_roster()
        await asyncio.sleep(1)
        
        logging.info(f"Sende Nachricht an {self.recipient}...")
        self.send_message(
            mto=self.recipient,
            mbody=self.message_text,
            mtype='chat'
        )
        
        await asyncio.sleep(2)
        logging.info("Übertragung erfolgreich.")
        self.disconnect()

async def run_bot(args, username, password):
    recipient_jid = args.to if "@" in args.to else f"{args.to}@127.0.0.1"
    jid = f"{username}@127.0.0.1"

    xmpp = StarfaceBot(jid, password, recipient_jid, args.msg)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    xmpp.ssl_context = ctx

    xmpp.register_plugin('xep_0030')
    xmpp.register_plugin('xep_0199')

    logging.info(f"Verbinde als {jid}...")
    xmpp.connect(host=args.host, port=5222)
    await xmpp.disconnected

def main():
    parser = argparse.ArgumentParser(description="Starface CLI Messenger (XMPP)")
    parser.add_argument("--host", required=True, help="IP der Starface Anlage")
    parser.add_argument("-u", "--user", required=True, help="Benutzer-ID")
    parser.add_argument("-t", "--to", required=True, help="Empfänger-Zustellnummer")
    parser.add_argument("-m", "--msg", required=True, help="Nachrichtentext")
    args = parser.parse_args()

    password = getpass("Starface Passwort: ")
    
    logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')

    try:
        asyncio.run(run_bot(args, args.user, password))
    except KeyboardInterrupt:
        print("\nAbgebrochen.")
    except Exception as e:
        logging.error(f"Fehler: {e}")

if __name__ == '__main__':
    main()
