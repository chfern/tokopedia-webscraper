def scrollscan_page(driver):
    page_height = driver.execute_script("return window.scrollMaxY")
    driver.execute_script("window.scrollTo(0, 0);")
    for i in range(0, page_height, 50):
        driver.execute_script("window.scrollTo(window.scrollX, {})".format(i))
