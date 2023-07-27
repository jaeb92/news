## 주요 언론사(신문사) 뉴스 분석
- 언론사 별 주요 7대 카테고리 뉴스를 분석
- 카테고리 별 주요 키워드 

### 1. 뉴스 메인 URL
- chosun(조선일보): https://www.chosun.com/
    - 뉴스세부내용 url: https://www.chosun.com/<category1>/<category2>/yyyy/mm/dd/<news_id>/
    - news_id: [0-9A-Z]{26}

- joongang(중앙일보): https://www.joongang.co.kr/
    - 세부 url: https://www.joongang.co.kr/article/<news_id>
    - news_id: [0-9]{8} ex. 25180554

- donga(동아일보): https://www.donga.com/news/
    <!-- - 세부카테고리 뉴스리스트: https://www.donga.com/news/<category1>/<category2>/ -->
    - 세부 url: https://www.donga.com/news/<category1>/article/all/yyyymmdd/<news_id>/[1|2] ex. 20230727/120437634/1

- seoul(서울신문): https://www.seoul.co.kr/news/newsList.php?section=
    - 세부 url: https://www.seoul.co.kr/news/newsView.php?id=<news_id>
    - news_id: yyyymmdd[0-9]{6} ex. 20230727500072

- khan(경향신문): https://www.khan.co.kr/
    - 세부 url: https://khan.co.kr/<category1>/<category2>/article/<news_id>
    - news_id: yyyymmddHHMM[0-9]{3} ex. 202307262158001

- maeil(매일신문): https://news.imaeil.com/
    - 세부 url: https://news.imaeil.com/page/view/<news_id>
    - news_id: yyyymmddHHMMSSf   ex. 2023072610292725460

- hani(한겨례신문): https://www.hani.co.kr/arti/

### 2. 뉴스 주요 7대 카테고리
- 정치, 경제, 국제, 사회, 문화, 연예, 스포츠

### 3. 언론사별 세부 카테고리
- 카테고리 파일위치: data/news_category.xlsx

### 3. html 태그 구조 분석(뉴스 기사 리스트))
1) 조선일보 
    - 리스트 테이블: \<div, class="story-feed">
    - 제목: \<a class="story-card__headline | box--margin-none text--black font--secondary h4 text__link--color">