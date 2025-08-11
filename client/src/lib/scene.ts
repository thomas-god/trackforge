import {
  DirectionalLight,
  Mesh,
  MeshPhongMaterial,
  PerspectiveCamera,
  Scene,
  WebGLRenderer,
  Group,
  AmbientLight,
  DoubleSide,
  Box3,
  Vector3
} from 'three';
import { STLLoader } from 'three/examples/jsm/Addons.js';

const scene = new Scene();

const loader = new STLLoader();

const camera = new PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

addLights(scene);

let renderer: WebGLRenderer;

const resize = () => {
  renderer.setSize(window.innerWidth / 2, window.innerHeight / 2);
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
};

export const createScene = (el: HTMLCanvasElement) => {
  renderer = new WebGLRenderer({ antialias: true, canvas: el });
  resize();
  renderer.render(scene, camera);
};

function addLights(scene: Scene) {
  // Add ambient light
  const ambientLight = new AmbientLight(0x404040, 0.6); // soft white light
  scene.add(ambientLight);

  // Add directional lights
  const directionalLight = new DirectionalLight(0xffffff, 0.6);
  directionalLight.position.set(0, -5, 10);
  scene.add(directionalLight);

  const directionalLightBis = new DirectionalLight(0xffffff, 0.6);
  directionalLight.position.set(5, 5, 10);
  scene.add(directionalLightBis);
}

export const addToScene = (stlContent: ArrayBuffer | undefined) => {
  if (stlContent === undefined) {
    return;
  }
  try {
    scene.clear();
    addLights(scene);
    const group = new Group();
    scene.add(group);

    const geometry = loader.parse(stlContent);

    const material = new MeshPhongMaterial({
      color: 0xffffff,
      side: DoubleSide
    });
    const mesh = new Mesh(geometry, material);
    geometry.center();
    geometry.computeVertexNormals();

    const box = new Box3().setFromObject(mesh);
    const size = box.getSize(new Vector3()).length();
    const scale = 10 / size;
    mesh.scale.setScalar(scale);
    mesh.position.set(0, 0, 0);

    group.add(mesh);

    camera.position.set(0, 0, 5);
    camera.lookAt(0, 0, 0);

    renderer.render(scene, camera);
  } catch (error) {
    console.log(error);
  }
};

window.addEventListener('resize', resize);
