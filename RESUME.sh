source /opt/conda/etc/profile.d/conda.sh
conda activate /workspaces/asi-env
export PYTHONPATH=/workspaces/ASI-Arch:$PYTHONPATH
echo "PyTorch: $(python -c 'import torch; print(torch.__version__)') CUDA: $(python -c 'import torch; print(torch.cuda.is_available())')"
python discovery_pipeline_v2.py
