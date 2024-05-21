import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotGenerator:
    def __init__(self, json_file):
        self.data = pd.read_json(json_file)
        # Creating folder for plots
        self.plots_dir = 'plots'
        os.makedirs(self.plots_dir, exist_ok=True)

    def draw_plots(self):
        plot_paths = []

        # creating plots for Mean Deviation
        mean_plot_path = os.path.join(self.plots_dir, 'mean_deviation.png')
        self.data.plot(x='name', y='mean', kind='bar', title='Mean Deviation by Room')
        plt.savefig(mean_plot_path)  # Saving plots
        plot_paths.append(mean_plot_path)
        plt.clf()

        # creating plots for Max Deviation by Room
        max_plot_path = os.path.join(self.plots_dir, 'max_deviation.png')
        self.data.plot(x='name', y='max', kind='bar', title='Max Deviation by Room')
        plt.savefig(max_plot_path)
        plot_paths.append(max_plot_path)
        plt.clf()  #

        # creating plots for Min Deviation by Room
        min_plot_path = os.path.join(self.plots_dir, 'min_deviation.png')
        self.data.plot(x='name', y='min', kind='bar', title='Min Deviation by Room')
        plt.savefig(min_plot_path)  # Сохранение графика в файл
        plot_paths.append(min_plot_path)
        plt.clf()  # Очистка текущего рисунка

        # comparing the number of corners with Ground Truth and finding models
        corners_plot_path = os.path.join(self.plots_dir, 'corners_comparison.png')
        self.data.plot(x='name', y=['gt_corners', 'rb_corners'], kind='bar', title='GT vs RB Corners')
        plt.savefig(corners_plot_path)
        plot_paths.append(corners_plot_path)
        plt.clf()

        return plot_paths


if __name__ == "__main__":
    json_file_path = 'https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'
    plot_gen = PlotGenerator(json_file_path)
    plot_paths = plot_gen.draw_plots()
    print(f'Plots saved at: {plot_paths}')


