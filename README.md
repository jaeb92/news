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
    - news_id: [0-9]{9}

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
    - 세부 url: https://www.hani.co.kr/arti/\<category1>/\<category2>/\<news_id>.html
    - news_id: [0-9]{7}

- hankook(한국일보): https://www.hankookilbo.com/
    - 세부 url: https://www.hankookilbo.com/News/Read/\<news_id>
    - news_id: [0-9A-Z]{20} ex. A2023072715420004839

### 2. 뉴스 주요 7대 카테고리
- 정치, 경제, 국제, 사회, 문화, 연예, 스포츠

### 3. 언론사별 세부 카테고리
- 카테고리 파일위치: data/news_category.xlsx

### 3. html 구조 분석
#### 3-1. 조선일보
> ##### - 뉴스 리스트페이지
>- url: https://www.chosun.com/\<category1>/\<category2>/
>>1. 뉴스리스트 테이블
>>- 태그명: div
>>- 클래스: story-feed
>>2. 뉴스리스트 제목
>>- 태그명: a
>>- 클래스: story-card__headline | box--margin-none text--black font--secondary h4 text__link--color
>>3. 뉴스리스트 내용 요약
>>- 태그명: div
>>- 클래스: story-card-component story-card__deck | text--grey-60 font--primary font--size-sm-14 font--size-md-14 text--line-height-1.43 text--overflow-ellipsis
>>4. 상세페이지 url
>>- 태그명: a
>>- 속성: href, ex. /\<category1>/\<category2>/\<yyyy>/\<mm>/\<dd>/\<news_id>
> ##### - 뉴스 상세페이지
>- url: https://www.chosun.com/\<category1>/\<category2>/\<yyyy>/\<mm>/\<dd>/\<news_id>
>>1. 뉴스제목
>>- 태그명: h1
>>- 클래스: article-header__headline
>>2. 뉴스본문
>>- 태그명: section
>>- 클래스: article-body
>>3. 기자
>>- 태그명: span
>>- 클래스: article-byline__author
>>4. 입력시간
>>- 태그명: span
>>- 클래스: inputDate
>>5. 업데이트
>>- 태그명: span
>>- 클래스: upDate
>>6. 본문 내 이미지
>>- 태그명: img
>>- 클래스: box--display-block cover

#### 3-2. 중앙일보
>##### - 뉴스 리스트페이지
>- url: https://www.joongang.co.kr/\<category1>/\<category2>
>>1. 뉴스리스트 테이블
>>- 태그명: ul
>>- 클래스: story_list
>>2. 뉴스리스트 제목
>>- 태그명: h2
>>- 클래스: headline
>>3. 뉴스리스트 본문 요약
>>- 태그명: p
>>- 클래스: description
>##### - 뉴스 상세페이지
>- url: https://www.joongang.co.kr/article/\<news_id>
>>1. 뉴스제목
>>- 태그명: h1
>>- 클래스: headline
>>2. 뉴스본문
>>- 태그명: div
>>- 클래스: article_body fs3
>>3. 기자
>>- 태그명: div
>>- 클래스: byline
>>4. 입력시간
>>- 태그명: p
>>- 클래스: date
>>5. 업데이트
>>- 태그명:
>>- 클래스:
>>6. 본문 내 이미지
>>- 태그명: div
>>- 클래스: ab_photo photo_center 

#### 3-3. 동아일보
>##### - 뉴스 리스트페이지
>- url: https://www.donga.com/news/\<category1>/\<category2>
>>1. 뉴스리스트 테이블
>>- 태그명: div
>>- 클래스: etcCon etcPage
>>2. 뉴스리스트 제목
>>- 태그명: span
>>- 클래스: tit
>>3. 뉴스리스트 본문 요약
>>- 태그명: span
>>- 클래스: txt
>##### - 뉴스 상세페이지
>- url: https://www.donga.com/news/\<category1>/article/all/\<yyyymmdd>/120433118/1
>>1. 뉴스제목
>>- 태그명: h1
>>- 클래스: title
>>2. 뉴스본문
>>- 태그명: div
>>- 클래스: article_txt
>>3. 기자
>>- 태그명: span
>>- 클래스: name
>>4. 입력시간 & 업데이트
>>- 태그명: span
>>- 클래스: date01
>>5. 본문 내 이미지
>>- 태그명: div
>>- 클래스: articlePhotoC

>#### 3-4. 서울신문
>##### - 뉴스 리스트페이지
>- url: https://www.seoul.co.kr/news/newsList.php?section=\<category2>
>>1. 뉴스리스트 테이블
>>- 태그명: div
>>- 클래스: S20_list_area 
>>2. 뉴스리스트 제목
>>- 태그명: div
>>- 클래스: tit lineclamp2
>>3. 뉴스리스트 본문 요약
>>- 태그명: div
>>- 클래스: sub lineclamp2
>##### - 뉴스 상세페이지
>- url: https://www.seoul.co.kr/news/newsView.php?id=\<news_id>
>>1. 뉴스 제목
>>- 태그명: h1
>>- 클래스: atit2
>>2. 뉴스 본문
>>- 태그명: div
>>- 클래스: S20_v_article
>>3. 기자
>>- 본문 태그 마지막 단락
>>4. 입력시간 & 업데이트
>>- 태그명: span
>>- 클래스: w_date
>>5. 본문 내 이미지
>>- 태그명: div
>>- 클래스: v_photo

>#### 3-5. 경향신문
>##### - 뉴스 리스트페이지
>- url: https://www.khan.co.kr/\<category1>/\<category2>/articles
>>1. 뉴스리스트 테이블
>>- 태그명: div
>>- 클래스: cont-main
>>2. 뉴스리스트 제목
>>- 태그명: h2
>>- 클래스: tit
>>3. 뉴스리스트 본문 요약
>>- 태그명: span
>>- 클래스: lead
>##### - 뉴스 상세페이지
>- url: https://www.khan.co.kr/\<category1>/\<category2>/article/\<news_id>
>>1. 뉴스 제목
>>- 태그명: h1
>>- 클래스: headline
>>2. 뉴스 본문
>>- 태그명: div
>>- 클래스: art_body
>>3. 기자
>>- 태그명: span
>>- 클래스: author
>>4. 입력시간 & 업데이트
>>- 태그명: div
>>- 클래스: byline
>>5. 본문 내 이미지
>>- 태그명: div
>>- 클래스: art_photo_wrap

>#### 3-6 매일신문
>##### - 뉴스 리스트페이지
>- url: https://news.imaeil.com/\<category2>
>>1. 뉴스리스트 테이블
>>- 태그명: ul
>>- 클래스: wcms_outline
>>2. 뉴스리스트 제목
>>- 태그명: p
>>- 클래스: title
>>3. 뉴스리스트 본문 요약
>>- 태그명: p
>>- 클래스: body
>##### - 뉴스 상세피이지
>- url: https://news.imaeil.com/page/view/\<news_id>
>>1. 뉴스제목
>>- 태그명: p
>>- 클래스: title
>>2. 뉴스본문
>>- 태그명: div
>>- 클래스: article_content
>>3. 기자
>>- 태그명: span
>>- 클래스: name
>>4. 입력시간 & 업데이트
>>- 태그명: span
>>- 클래스: date
>>5. 본문 내 이미지
>>- 태그명: figure
>>- 클래스: img_center

>#### 3-7 한겨례신문
>##### - 뉴스 리스트페이지
>- url: https://www.hani.co.kr/arti/\<category1>/\<category2>/home01.html
>>1. 뉴스리스트 테이블
>>- 태그명: div
>>- 클래스: section-list-area photo-view3
>>2. 뉴스리스트 제목
>>- 태그명: h4
>>- 클래스: article-title
>>3. 뉴스리스트 본문 요약
>>- 태그명: -
>>- 클래스: -
>##### - 뉴스 상세페이지
>- url: https://www.hani.co.kr/arti/\<category1>/\<category2>/\<news_id>.html
>>1. 뉴스 제목
>>- 태그명: span
>>- 클래스: title
>>2. 뉴스 본문
>>- 태그명: div
>>- 클래스: article-text
>>3. 기자
>>- 태그명: div
>>- 클래스: kiza-info
>>4. 입력시간 & 업데이트
>>- 태그명: p
>>- 클래스: date-time
>>5. 본문 내 이미지
>>- 태그명: div
>>- 클래스: imageC

>#### 3-8 한국일보
>##### - 뉴스 리스트페이지
>- url: https://www.hankookilbo.com/News/\<category1>/\<category2>
>>1. 뉴스리스트 테이블
>>- 태그명: ul
>>- 클래스: board-list column-3
>>2. 뉴스리스트 제목
>>- 태그명: h3
>>- 클래스:
>##### - 뉴스 상세페이지
>- url: https://www.hankookilbo.com/News/Read/\<news_id>
>>1. 뉴스 제목
>>- 태그명: h2
>>- 클래스: title
>>2. 뉴스 본문
>>- 태그명: p
>>- 클래스: editor-p
>>3. 기자
>>- 태그명: span
>>- 클래스: nm
>>4. 입력시간 & 업데이트
>>- 태그명: dl
>>- 클래스: wrt-text
>>5. 본문 내 이미지
>>- 태그명: div
>>- 클래스: editor-img-box