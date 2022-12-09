from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = "drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.viajesexito.com")

# close_btn = driver.find_element(By.XPATH, '/html/body/div[36]/div/div/div[1]/button')
# close_btn.click();
time.sleep(0.5)

package_btn = driver.find_element(By.XPATH, "/html/body/form/header/div[2]/div/div/nav/div[2]/a")
package_btn.click()

time.sleep(2)

input_vuelo_hotel = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div/ul/li[1]/label/input')

to = "Punta Cana, Republica Dominicana (PUJ)";
search_input = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input')
search_input.click()
search_input.send_keys(to)

time.sleep(0.5)


calendar_input = driver.find_element(By.XPATH,  '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/input')
calendar_input.click()
time.sleep(.5)
dec_14 = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a')
dec_14.click()


dec_22 = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a')
dec_22.click()

bed_input = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p')
bed_input.click()

plus = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button/span')
plus.click()

apply_btn = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button')
apply_btn.click()

search_btn = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a')
search_btn.click();

time.sleep(20)

res1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/a/div/div[2]/span[2]').text
res2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/a/div/div[2]/span[2]').text
res3 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[4]/a/div/div[2]/span[2]').text
res4 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/a/div/div[2]/span[2]').text
res5 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/a/div/div[2]/span[2]').text
res6 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[4]/div[3]/a/div/div[2]/span[2]').text
res7 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[4]/div[4]/a/div/div[2]/span[2]').text
res8 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[5]/div[3]/a/div/div[2]/span[2]').text

list = [res1, res2, res3, res4, res5, res6, res7, res8]

print("\n-------Productos de la primer pagina en consola-------\n");
for n in range(8):
    print("Precio del vuelo #" + list[n] + "\n")

airline = "Air Canada (AC)";

airline_input = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')

airline_input.click()
airline_input.send_keys(airline)

new_search_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')

new_search_btn.click()
    
time.sleep(20)

driver.close()
driver.quit()


