<?php

class Path {
    public $currentPath;

    public function __construct($path) {
        $this->currentPath = $path;
    }

    public function cd($newPath) {
        // Split the current path and new path into arrays
        $currentDirs = explode('/', $this->currentPath);
        $newDirs = explode('/', $newPath);

        // Process each directory in the new path
        foreach ($newDirs as $dir) {
            // Handle the parent directory ('..')
            if ($dir === '..') {
                array_pop($currentDirs); // Move up one level
            } else {
                // Handle regular directory names
                $currentDirs[] = $dir;
            }
        }

        // Rebuild the current path
        $this->currentPath = implode('/', $currentDirs);
    }
}

// Example usage
$path = new Path('/Users/n3ll1x/shared/Documenti/projects/iliad/task3/change_directory.php');
$path->cd('../');
echo $path->currentPath;

?>
