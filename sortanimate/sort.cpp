#include <SFML/Graphics.hpp>
#include <vector>
#include <chrono>
#include <thread>

void print(std::vector<sf::RectangleShape>& rectangles, sf::RenderWindow& window) {
    window.clear();
    for (const auto& rectangle : rectangles) {
        window.draw(rectangle);
    }
    window.display();
    std::this_thread::sleep_for(std::chrono::milliseconds(500));
}

void bubbleSort(std::vector<int>& data, std::vector<sf::RectangleShape>& rectangles, sf::RenderWindow& window) {
    for (size_t i = 0; i < data.size(); i++) {
        for (size_t j = 0; j < data.size() - i - 1; j++) {
            if (data[j] > data[j + 1]) {
                std::swap(data[j], data[j + 1]);
                std::swap(rectangles[j], rectangles[j + 1]);
                print(rectangles, window);
            }
        }
    }
}

int main()
{
    // Create a window
    sf::RenderWindow window(sf::VideoMode(800, 600), "Sorting Animation");

    // Create a vector to hold the data
    std::vector<int> data = {30, 50, 10, 40, 20};

    // Create a vector to hold the rectangles
    std::vector<sf::RectangleShape> rectangles;

    // Create the rectangles
    for (int i = 0; i < data.size(); i++) {
        sf::RectangleShape rectangle(sf::Vector2f(50, data[i] * 10));
        rectangle.setPosition(i * 60, 600 - data[i] * 10);
        rectangles.push_back(rectangle);
    }

    // Sort the data and animate the sorting process
    bubbleSort(data, rectangles, window);

    // Game loop
    while (window.isOpen())
    {
        // Process events
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Clear the window
        window.clear();

        // Draw the rectangles
        for (const auto& rectangle : rectangles) {
            window.draw(rectangle);
        }

        // Display the window
        window.display();
    }

    return 0;
}