import { globby, path } from 'vuepress/utils';
export const getComponentsFromDir = async ({ componentsDir, componentsPatterns = ['**/*.vue'], getComponentName = (filename) => path.trimExt(filename.replace(/\/|\\/g, '-')), }) => {
    if (!componentsDir) {
        return {};
    }
    // get all matched component files
    const componentsDirFiles = await globby(componentsPatterns, {
        cwd: componentsDir,
    });
    // transform files to name => filepath map
    return Object.fromEntries(componentsDirFiles.map((filename) => [
        getComponentName(filename),
        path.resolve(componentsDir, filename),
    ]));
};
