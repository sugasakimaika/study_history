import logging
import os

# ログディレクトリの作成
log_dir = 'data/logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# ログ設定
logging.basicConfig(
    filename=os.path.join(log_dir, 'my_app.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ログの記録
logging.info('This is an informational message.')
logging.warning('This is a warning message.')
logging.error('This is an error message.')
