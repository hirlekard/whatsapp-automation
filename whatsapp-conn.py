from WPP_Whatsapp import Create
import time


def safe_execute(func, retries=3):
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            print(f" Retry {i+1}/{retries}: {e}")
            time.sleep(5)
    return None


def get_group_members(client, group_id):

    def _fetch():
        members = client.getGroupMembers(group_id)

        result = set()

        for m in members:
            jid = m.get("id")

            if isinstance(jid, dict):
                jid = jid.get("_serialized")

            if jid:
                result.add(jid.strip().lower())

        return result

    return safe_execute(_fetch) or set()


def add_member(client, group_id, member):

    def _add():
        return client.addParticipant(group_id, member)

    res = safe_execute(_add)

    if res:
        print(f"Added: {member}")
    else:
        print(f" Failed: {member}")

    time.sleep(2)


def run():

    client = Create(session="community_bot").start()

    print(" Stabilizing session...")
    time.sleep(25)

    groups = [
        "120363408417477198@g.us",
        "120363427181465444@g.us"
    ]

    members = [
        "6588760367@c.us",
        "6590827203@c.us",
        "6598807981@c.us",
        "6581897501@c.us"
    ]

    for g in groups:

        print("\n==============================")
        print("Processing group:", g)
        print("==============================")

        existing = get_group_members(client, g)

        print(f" Existing members: {len(existing)}")

        for m in members:

            if m.strip().lower() in existing:
                print(f" Skipping (already exists): {m}")
                continue

            add_member(client, g, m)

    print("\n Done!")


if __name__ == "__main__":
    run()
