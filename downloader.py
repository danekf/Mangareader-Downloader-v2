import fitz
import base64
from utils import ElementExists
from selenium.webdriver.common.by import By
from time import sleep
import selenium

valiad_check_chars = [b'`\x82', b'\xff\xd9', b"\x00\x00", b"ds"]

def DownloadVolume(driver, next_btn, rating_panel_path, foldername, next_btn_path):

    page = 1

    last_url = driver.current_url
    retry_attempts = 0
    max_attempts = 30

    tot_pages_selector = "#divslide > div.navi-buttons.hoz-controls.hoz-controls-rtl > div.nabu-page > span > span.hoz-total-image"

    tot_pages = driver.find_element(by=By.CSS_SELECTOR, value=tot_pages_selector)

    while True:
        print(f"On page {page}")
        pdfdata = driver.print_page()
        doc = fitz.Document(stream=base64.b64decode(pdfdata))

        images = doc.get_page_images(0)

        if len(images) < 2:
            if retry_attempts > max_attempts:
                print("New volume!")
                break;
                    
            print(f"No images found, retrying after 0.5 seconds. Retry attempt: {retry_attempts}")
            sleep(0.5)
            retry_attempts += 1
            continue

        img = list(images)[1]
        xref = img[0]
        image = doc.extract_image(xref)
        print("Pix.save() ", end="")
        print(type(image))
        check_chars = image["image"][-2:]
        if check_chars in valiad_check_chars:
            pass
        else:
            print('Not complete image')
            print(check_chars)
            sleep(0.5)
            continue
        pix = fitz.Pixmap(doc, xref)
        pix.save(f"temp/{foldername}/{page}.png")
        page += 1
        retry_attempts = 0
        # driver.execute_script("hozNextImage();");

        driver.execute_script("hozNextImage();");

        """
        try:
            next_btn.click()
        except selenium.common.exceptions.StaleElementReferenceException:
            next_btn = driver.find_element(By.CSS_SELECTOR, value=next_btn_path)
            try:
                next_btn.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                sleep(5)
                # next_btn = driver.find_element(By.CSS_SELECTOR, value=next_btn_path)
                # next_btn.click()
                driver.execute_script("hozNextImage();")
        """
