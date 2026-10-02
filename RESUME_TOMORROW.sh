#!/bin/bash
cd /workspaces/ASI-Arch
source /opt/conda/etc/profile.d/conda.sh
conda activate /workspaces/asi-env
export PYTHONPATH=/workspaces/ASI-Arch:$PYTHONPATH

echo "=== RESUMING ==="
python -c "import torch; print(f'PyTorch: {torch.__version__} CUDA: {torch.cuda.is_available()}')"
echo "Pipeline test:"
python -c "from pipeline.pipeline import Pipeline; print('✓ Pipeline OK')"
echo ""
echo "To run real discovery with Gemini:"
echo "1. Add key: echo 'GEMINI_API_KEY=your_key' > .env"
echo "2. Run: python discovery_pipeline_v2.py"
echo ""
echo "Last blueprint:"
cat discovered_architecture.json
