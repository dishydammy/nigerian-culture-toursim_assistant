import wikipedia
import json
from pathlib import Path
from utils.cleaning import clean_text

RAW_DIR = Path("data/raw")

# Topics for Wikipedia
TOPICS = [
    # Yoruba
    "Yoruba culture", "Ooni of Ife", "Alaafin of Oyo", "Oba of Benin",
    "Ife bronzes", "Oduduwa", "Osun-Osogbo Sacred Grove", "Sango", "Ifa divination", "Orisa",
    # Hausa-Fulani
    "Hausa-Fulani culture", "Durbar festival", "Emir's palace", "Sharo festival",
    "Sultan of Sokoto", "Argungu fishing festival", "Bida brass works", "Kano City Walls",
    # Igbo
    "Igbo culture", "Ofala festival", "Igbo-Ukwu bronzes", "New Yam Festival", "Mmanwu",
    "Ojukwu", "Eze Nri", "Nkwobi", "Ohafia War Dance",
    # Other ethnic groups
    "Efik people", "Ibibio people", "Tiv people", "Edo people", "Ijaw people",
    "Kanuri people", "Nupe people", "Urhobo people",
    # Festivals
    "Eyo Festival", "Osun-Osogbo Festival", "Ojude Oba", "Calabar Carnival", "Felabration",
    "Lagos Fashion Week", "Ake Arts and Book Festival", "Lagos International Jazz Festival",
    # Historical sites
    "Sukur Cultural Landscape", "National Museum Lagos", "Olumo Rock",
    "Ancient Kano City Walls", "Benin City Walls and Moat", "Gashaka-Gumti National Park",
    "Ogbunike Caves", "First Storey Building in Nigeria", "Jaekel House", "Oba of Benin Palace",
    "Zuma Rock", "Lekki Conservation Centre", "Iga Idunganran", "Oke Idanre Hill",
    "Tafawa Balewa Square", "Nike Art Gallery", "Gurara Waterfalls",
    # Arts & crafts
    "Nok terracotta", "Benin bronzes", "Ife heads", "Igbo-Ukwu art",
    "Calabash carving", "Adire", "Akwete cloth", "Ladi Kwali", "Yoruba beadwork", "Wood carving",
    # Attire
    "Aso-oke", "Buba and Iro", "Agbada", "Dandogo", "Gele", "Fila", "Shokoto",
    # Cuisine
    "Jollof Rice", "Pounded Yam", "Egusi Soup", "Efo Riro", "Amala and Gbegiri",
    "Tuwo Shinkafa", "Suya", "Akara", "Moi-moi", "Pepper soup",
    "Zobo drink", "Palm wine", "Kunu drink", "Fura de nunu",
    "Chin Chin", "Puff Puff", "Fried plantain", "Kuli-kuli"
]

def collect_wikipedia():
    all_docs = []
    for topic in TOPICS:
        try:
            page = wikipedia.page(topic)
            cleaned_content = clean_text(page.content)
            all_docs.append({
                "title": page.title,
                "content": cleaned_content,
                "url": page.url
            })
            print(f"✔ Collected: {topic}")
        except Exception as e:
            print(f"✘ Failed: {topic} — {e}")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_file = RAW_DIR / "wikipedia_data.json"
    out_file.write_text(json.dumps(all_docs, ensure_ascii=False, indent=2))
    print(f"Saved {len(all_docs)} Wikipedia docs to {out_file}")

if __name__ == "__main__":
    collect_wikipedia()
