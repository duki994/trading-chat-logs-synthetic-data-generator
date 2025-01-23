import json
import random
import uuid
from datetime import datetime, timedelta


class RegulatoryFlags:
    SUSPICIOUS_ACTIVITY = 1 << 0
    INSIDER_TRADING = 1 << 1
    WASH_TRADING = 1 << 2
    MANIPULATION = 1 << 3
    HIGH_FREQUENCY = 1 << 4
    CROSS_MARKET = 1 << 5
    LATE_TRADE = 1 << 6

    def __init__(self):
        self.flags = 0

    def set_flag(self, flag):
        self.flags |= flag
        return self

    def clear_flag(self, flag):
        self.flags &= ~flag
        return self

    def has_flag(self, flag):
        return bool(self.flags & flag)
    
    def get_alerts(self):
        flag_map = {
            self.SUSPICIOUS_ACTIVITY: "SUSPICIOUS",
            self.INSIDER_TRADING: "INSIDER",
            self.WASH_TRADING: "WASH",
            self.MANIPULATION: "MANIP",
            self.HIGH_FREQUENCY: "HFT",
            self.CROSS_MARKET: "CROSS",
            self.LATE_TRADE: "LATE"
        }
        return [flagDescription for flag,flagDescription in flag_map.items() if self.flags & flag]


class TradingChatGenerator:
    # def __init__(self):
    #     self.tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "META"]
    #     self.traders = [
    #         "trader1",
    #         "trader2",
    #         "trader3",
    #         "trader4",
    #         "trader5",
    #         "analyst1",
    #         "analyst2",
    #         "analyst3",
    #         "pm1",
    #     ]
    #     self.order_types = ["market", "limit", "stop", "dark_pool", "block"]
    #     self.order_flow_patterns = {
    #         "sweep": {"desc": "Multiple exchange sweep", "prob": 0.2},
    #         "iceberg": {"desc": "Hidden liquidity", "prob": 0.15},
    #         "peg": {"desc": "Pegged to VWAP", "prob": 0.3},
    #         "dark": {"desc": "Dark pool execution", "prob": 0.25},
    #         "block": {"desc": "Large block trade", "prob": 0.1},
    #     }

    def __init__(self, config):
        self.tickers = [ticker for sector in config['tickers'].values() for ticker in sector]
        self.traders = [trader for role in config['traders'].values() for trader in role]
        self.order_flow = config['order_flow']

    def generate_order_flow(self):
        pattern = random.choices(
            list(self.order_flow.keys()),
            weights=[p['prob'] for p in self.order_flow.values()]
        )[0]
        flow_config = self.order_flow[pattern]
        
        return {
            "msgw_id": f"MSGW_{uuid.uuid4()}",
            "pattern": pattern,
            "description": flow_config['desc'],
            "size": random.randint(flow_config['min_size'], flow_config['min_size']*2),
            "exchanges": random.sample(flow_config['exchanges'], 
                                    random.randint(1, len(flow_config['exchanges']))),
            "order_type": random.choice(['market', 'limit', 'stop', 'dark_pool', 'block']),
            "mifid_fields": {
                "trading_capacity": random.choice(["DEAL", "MATCH", "AOTC"]),
                "liquidity_provision": random.choice([True, False]),
                "dma_flag": random.choice([True, False])
            }
        }

    def generate_regulatory_check(self):
        reg_flags = RegulatoryFlags()
        if random.random() < 0.1:
            num_flags = random.randint(1, 3)  # max 3 flags
            flags = [
                RegulatoryFlags.SUSPICIOUS_ACTIVITY,
                RegulatoryFlags.INSIDER_TRADING,
                RegulatoryFlags.WASH_TRADING,
                RegulatoryFlags.MANIPULATION,
                RegulatoryFlags.HIGH_FREQUENCY,
                RegulatoryFlags.CROSS_MARKET,
                RegulatoryFlags.LATE_TRADE,
            ]
            selected_flags = random.sample(flags, num_flags)  # select random 3 flags
            for flag in selected_flags:
                reg_flags.set_flag(flag)

        return {
            "flags": reg_flags.flags,
            "alerts": reg_flags.get_alerts(),
            "timestamp": datetime.now().isoformat(),
        }

    def generate_trade_chat(self, num_entries=1000):
        chats = []
        start_date = datetime(2024, 1, 1)  # Janurary 1st, 2024

        for _ in range(num_entries):
            timestamp = start_date + timedelta(
                days=random.randint(0, 365), seconds=random.randint(0, 86400)
            )

            entry = {
                "timestamp": timestamp.isoformat(),
                "trader": random.choice(self.traders),
                "ticker": random.choice(self.tickers),
                "price": round(random.uniform(50, 500), 2),
                "volume": random.randint(100, 1000000),
                "order_flow": self.generate_order_flow(),
                "regulatory": self.generate_regulatory_check(),
            }
            chats.append(entry)

        # sort by timestamp. not necessary but makes it easier to read
        return sorted(chats, key=lambda x: x["timestamp"])

    def save_as_json(self, chats, filename="synthetic_trading_chats.json"):
        with open(filename, "w") as f:
            json.dump(
                {
                    "chats": chats,
                    "metadata": {
                        "generated": datetime.now().isoformat(),
                        "version": "2.1",
                        "num_entries": len(chats),
                    },
                },
                f,
                indent=2,
            )

