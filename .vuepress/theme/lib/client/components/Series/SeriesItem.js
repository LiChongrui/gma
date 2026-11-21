import { h } from 'vue';
import { IconFolder } from '@components/icons/index.js';
import { useRoute } from 'vuepress/client';
import Link from '../Link.vue';
import Xicons from '../global/Xicons.vue';
const normalizePath = (path) => decodeURI(path)
    .replace(/#.*$/, '')
    .replace(/(index)?\.(md|html)$/, '');
const isActiveLink = (route, link) => {
    if (link === undefined) {
        return false;
    }
    if (route.hash === link) {
        return true;
    }
    const currentPath = normalizePath(route.path);
    const targetPath = normalizePath(link);
    return currentPath === targetPath;
};
// 组自身带 link 时（如 crs.ProjMethods 组标题即总览页），链接页也算激活
const isActiveItem = (route, item) => {
    if (item.children) {
        return item.children.some((child) => isActiveItem(route, child))
            || isActiveLink(route, item.link);
    }
    if (isActiveLink(route, item.link)) {
        return true;
    }
    return false;
};
// 一、二级组渲染组标题；仅一级组或显式 collapsable 的二级组才有折叠交互与箭头
// （二级组默认常驻展开，无箭头，如 crs > ProjMethods）
const isCollapsibleGroup = (item, level) => !!item.children && level <= 2;
const canCollapse = (item, level) =>
    isCollapsibleGroup(item, level)
        && (level === 1 || !!(item.collapsable ?? item.collapsible));
const togglecollapsible = (e, item, level) => {
    if (!canCollapse(item, level))
        return;
    item.collapsible = !!!item.collapsible;
    const currentNode = e.target.closest('.series-heading');
    const arrowNode = currentNode.querySelector('.arrow');
    const nextNode = currentNode.nextElementSibling;
    if (item.collapsible) {
        arrowNode.classList.remove('down');
        arrowNode.classList.add('right');
        nextNode.style.display = 'none';
    }
    else {
        arrowNode.classList.remove('right');
        arrowNode.classList.add('down');
        nextNode.style.display = 'block';
    }
};
const renderItem = (item, level, props) => {
    // 组标题：一级组（folder 图标 + 纯文本）与二级组（文本可带链接）都渲染折叠箭头。
    // 带 link 的组：点击标题文本跳转链接，点击箭头折叠/展开（两个独立点击区）
    if (isCollapsibleGroup(item, level)) {
        const titleTag = level === 1 ? 'h5' : 'h6';
        const collapsible = canCollapse(item, level);
        const heading = [
            item.link
                ? h(Link, { item, class: 'series-group-title-link' })
                : h(Xicons, {
                    icon: level === 1 ? IconFolder : '',
                    text: item.text,
                    textSize: level === 1 ? 16 : 14
                }),
            collapsible
                ? h('span', {
                    class: !!item.collapsible ? 'arrow right' : 'arrow down',
                    ...(item.link
                        ? { onClick: (e) => togglecollapsible(e, item, level) }
                        : {}),
                })
                : null,
        ];
        return h(titleTag, {
            ...props,
            ...(collapsible && !item.link
                ? { onClick: (e) => togglecollapsible(e, item, level) }
                : {}),
        }, heading);
    }
    if (item.link) {
        return h(Link, {
            ...props,
            item,
        });
    }
    const titleTag = level === 1 ? 'h5' : 'h6';
    // if the item only has text, render it as `<p>`
    return h(titleTag, { ...props }, [
        h(Xicons, {
            icon: level === 1 ? IconFolder : '',
            text: item.text,
            textSize: level === 1 ? 16 : 14
        }),
    ]);
};
const renderChildren = (item, level) => {
    if (!item.children?.length) {
        return null;
    }
    return h('ul', {
        style: {
            display: !!item.collapsible ? 'none' : 'block',
        },
    }, item.children.map((child) => h('li', h(SeriesItem, {
        item: child,
        level
    }))));
};
export const SeriesItem = ({ item, level }) => {
    const route = useRoute();
    // 二级组激活态：当前页落在组内（含组自身 link）则高亮组标题
    const active = isCollapsibleGroup(item, level) ? isActiveItem(route, item) : false;
    // 初始折叠状态：collapsible（运行时态，用户点过箭头）优先；
    // 否则取配置 collapsable，但当前路由在组内时强制展开（自动定位）
    if (isCollapsibleGroup(item, level)
        && item.collapsible === undefined
        && item.collapsable !== undefined) {
        item.collapsible = !!item.collapsable && !isActiveItem(route, item);
    }
    if (item.children) {
        return [
            h('section', {
                class: 'series-group series-item',
            }, [
                renderItem(item, level, {
                    class: {
                        'series-heading': true,
                        [`series-level-${level}`]: true,
                        active,
                    },
                }),
                renderChildren(item, ++level),
            ]),
        ];
    }
    return [
        renderItem(item, ++level, {
            class: {
                'series-item': true,
                active,
            },
        }),
    ];
};
SeriesItem.displayName = 'SeriesItem';
SeriesItem.props = {
    item: {
        type: Object,
        required: true,
    },
    level: {
        type: Number,
        required: true,
    },
};
