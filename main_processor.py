import json
import logging
from quixstreams import Application


def main():
    logging.info("START")
    app = Application(
        broker_address="kafka:9092",
        loglevel="DEBUG",
        auto_offset_reset="earliest",
        consumer_group="weather_processor",   
    )
    input_topic = app.topic("weather_data_demo")
    output_topic = app.topic("weather_i18n")

    def i18n_weather(msg):
        celsius = msg['current']['temperature_2m']
        farenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        new_msg = {
           "celsius":celsius, 
           "farenheit":round(farenheit,2), 
           "kelvin":round(kelvin,2), 
        }

        logging.debug("Returning: %s", new_msg)

        return new_msg

    streamingDataFrame = app.dataframe(input_topic)
    
    newStreamingDataFrame = streamingDataFrame.apply(i18n_weather)
    newStreamingDataFrame = newStreamingDataFrame.to_topic(output_topic)

    app.run(newStreamingDataFrame)

    
if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()