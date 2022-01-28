from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt


if __name__ == '__main__':
    noise1 = PerlinNoise(octaves=10)
    noise2 = PerlinNoise(octaves=6)
    noise3 = PerlinNoise(octaves=12)
    noise4 = PerlinNoise(octaves=24)

    xpix, ypix = 100, 100
    pic = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val = noise1([i / xpix, j / ypix])
            #noise_val += 0.5 * noise2([i / xpix, j / ypix])
            #noise_val += 0.25 * noise3([i / xpix, j / ypix])
            #noise_val += 0.125 * noise4([i / xpix, j / ypix])

            row.append(noise_val)
        pic.append(row)

    plt.imshow(pic, cmap='gray')
    plt.show()([0.5, 0.5, 0, 0, 0])