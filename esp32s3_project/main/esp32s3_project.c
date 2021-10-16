// H2install library (.h file)  https://vcpkg.io/en/getting-started.html
#include <stdio.h>
#include <stdlib.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"
#include "driver/gpio.h"
#include "led_strip.h"

#define BLINK_GPIO 48

static led_strip_t *pStrip_a;
uint8_t R,G,B;

static void configure_led(void)
{
    /* LED strip initialization with the GPIO and pixels number*/
    pStrip_a = led_strip_init(0, BLINK_GPIO, 1);
    /* Set all LED off to clear all pixels */
    pStrip_a->clear(pStrip_a, 50);
}

void app_main(void)
{
    char *ourTaskName = pcTaskGetName(NULL);
    ESP_LOGI(ourTaskName, "Starting UP...\n");
    configure_led();
    printf("this is prinf() function!\n\n");

    while (1){
        
        ESP_LOGI(ourTaskName, "COLOR R:%d G:%d B%d", R = rand()%12, G = rand()%12, B = rand()%12);
        /* Set the LED pixel using RGB from 0 (0%) to 255 (100%) for each color */
        pStrip_a->set_pixel(pStrip_a, 0, R, G, B);
        /* Refresh the strip to send data */
        pStrip_a->refresh(pStrip_a, 100);
        vTaskDelay(1000 / portTICK_PERIOD_MS);

        ESP_LOGI(ourTaskName, "Turn OFF.");
        /* Set all LED off to clear all pixels */
        pStrip_a->clear(pStrip_a, 50);
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
