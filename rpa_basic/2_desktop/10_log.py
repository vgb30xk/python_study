# import logging

# logging.basicConfig(level=logging.ERROR,
#                     format="%(asctime)s [%(levelname)s] %(message)s")
# logging.debug("에구.... 이거 누가 짰어??")
# logging.info("자동화 수행 준비")
# logging.warning("실행상의 문제가 있을 수 있습니다.")
# logging.error("에러가 발생하였습니다. 에러 코드는 ")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다")


# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
# 시간 메시지 형태로
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스크림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트 진행")
