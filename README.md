## Алгоритм распознавания
Задача алгоритма - сформировать линию на каждом кадре, указывающую направление необходимого движения и выдать угол её наклона (в диапазоне от 0 до 180 градусов).
Исходное изображение выглядит следующим образом:

![original.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/original.png)

1. Конвертируем его в формат HSV. Так мы сможем задать диапазон распознаваемых цветов;

![hsv.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/hsv.png)

2. Создаём маску для выделения синих областей из заданного диапазона цветов;

![mask.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/mask.png)

3. С помощью детектора границ Кенни находим углы на полученном изображении;

![canny edge detector.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/canny%20edge%20detector.png)

4. Избавляемся от лишних границ, оставляя только дорожную разметку;

![no noize.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/no%20noize.png)

5. С помощью преобразования Хафа получаем координаты линий на изображении;

![coordinates.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/coordinates.png)

6. Поскольку на пункте 5 мы получаем координаты не двух линий, а целой кучи, то необходимо их преобразовать в координаты нужных нам двух линий;

### Логика расчёта линий
Берём по очереди каждую задетектированную линию и проверяем, если она входит в левую часть изображения и наклонена вправо, то это левая линия. Сохраняем её наклон(slope) и пересечение(intercept) в массив. 
Если же линия входит в правую часть экрана и наклонена влево, то это правая линия. Сохраняем её наклон(slope) и пересечение(intercept) в другой массив. 
Так делаем с каждой линией и далее берём среднее по каждому массиву – это и будут искомые наклон(slope) и пересечение(intercept) двух полос. После этого нарисуем эти линии поверх исходного изображения.

![lane lines.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/lane%20lines.png)

![one lane line.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/one%20lane%20line.png)

7. Теперь, когда мы имеем координаты начала и конца обеих полос, считаем угол направляющей линии.

### Логика расчёта угла наклона
Для расчёта направляющей линии мы просто усредняем две линии по координатам конечных точек, получая координаты направляющей линии. Её наклон и будет углом поворота.
В случае если линия задетектирована всего одна, то углом поворота будет угол наклона этой же линии.

![direction line.png](https://github.com/Tpoc311/AutoPiCar/blob/master/Images/direction%20line.png)

## Инструменты и библиотеки
В проекте были использованы Python 3.7.3 и библиотека OpenCV 3.4.3.

## Источники

1. DeepPiCar — Part 1: How to Build a Deep Learning, Self Driving Robotic Car on a Shoestring Budget. URL: https://towardsdatascience.com/deeppicar-part-1-102e03c83f2c
