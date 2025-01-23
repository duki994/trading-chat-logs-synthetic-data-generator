import tradingConfig
from tradeChatGenerator import TradingChatGenerator


tcg = TradingChatGenerator(tradingConfig.get_config())

chats = tcg.generate_trade_chat(25)
tcg.save_as_json(chats, "synthetic_trading_chats.json")
