import os, sys, json, ccxt
ROOT = "/workspaces/ASI-Arch"
sys.path.insert(0, ROOT)
os.environ["PYTHONPATH"] = ROOT

print("--- STEP 1: FETCHING KUCOIN MARKET DATA ---")
kucoin = ccxt.kucoin({'enableRateLimit': True})
kucoin.load_markets()
print(f"Loaded {len(kucoin.markets)} markets")

candidates = [
  {"id": "USDT-BTC-ETH", "legs": ["BTC/USDT", "ETH/BTC", "ETH/USDT"]},
  {"id": "USDT-BTC-SOL", "legs": ["BTC/USDT", "SOL/BTC", "SOL/USDT"]},
]

market_data = {}
for t in candidates:
    try:
        if all(leg in kucoin.markets for leg in t["legs"]):
            # KuCoin requires limit=20 or 100, not 5
            ob1 = kucoin.fetch_order_book(t["legs"][0], limit=20)
            market_data[t["id"]] = {t["legs"][0]: {"top_ask": ob1['asks'][0] if ob1['asks'] else None}}
            print(f"✓ {t['id']}: {ob1['asks'][0] if ob1['asks'] else 'no asks'}")
    except Exception as e:
        print(f"✗ {t['id']}: {e}")

print(f"Mapped {len(market_data)} triangles")

print("\n--- STEP 2: BOOTING FIXED ASI-ARCH ---")
import torch
print(f"CUDA: {torch.cuda.is_available()} (expected False in Codespace)")
print(f"PyTorch: {torch.__version__}")

try:
    from pipeline.pipeline import Pipeline
    print("✓ Pipeline imported")

    task = f"Design HFT arb topology for {json.dumps(market_data)[:2000]}. Output JSON blueprint."
    print(f"Task: {task[:200]}...")

    pipeline = Pipeline(task_prompt=task)
    arch = pipeline.run()

    out_path = "/workspaces/output/discovered_architecture.json"
    os.makedirs("/workspaces/output", exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(arch if not isinstance(arch, str) else {"raw": arch}, f, indent=2)
    print(f"✅ SUCCESS: {out_path}")

except Exception as e:
    import traceback
    print(f"Import/run failed: {e}")
    traceback.print_exc()
